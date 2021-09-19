import argparse, math, os, re
from random import choice, randint, uniform
from concurrent.futures import ProcessPoolExecutor

# Number range
MIN_RANGE = 0
MAX_RANGE = 9999999999

# String length
MIN_LENGTH = 4
MAX_LENGTH = 40

def appendWhitespace(string: str):
    try:
        if type(string) != str:
            raise TypeError

        for _ in range(0, randint(1,10)):
            string += " "
        return string
    except TypeError:
        print(f"TypeError on '{appendWhitespace.__name__}(string)': string should be str but it receives '{string}' instead")
        raise
    except Exception as e:
        print(e)
        raise

def isFileExists(path: str, iteration: int = 1) -> str:
    if not os.path.exists(path):
        return path

    temp = path
    path = re.sub(r"-[0-9]+", "", temp)

    arr = path.split('.')
    iteration+=1

    if len(arr) > 1:
        arr[0] += f"-00{iteration}"
        extension = f".{arr[-1]}"
        arr[-1] = extension
        newPath = ""
        for string in arr:
            newPath += string
        return isFileExists(newPath, iteration)
    else:
        newPath = f"{path}-00{iteration}"
        return isFileExists(newPath, iteration)

def randchar():
    uppercase = chr(randint(65,90))
    lowercase = chr(randint(97,122))
    return choice([uppercase, lowercase])

def integer(*_):
    return randint(MIN_RANGE, MAX_RANGE)

def realnumber(*_):
    return uniform(MIN_RANGE, MAX_RANGE)

def alphaNumeric(length: int):
    try:
        string = ""
        string += appendWhitespace(string)
        for _ in range(0, length):
            number = str(randint(0,9))
            alphabet = randchar()
            string += choice([alphabet, number])
        return appendWhitespace(string)
    except TypeError as e:
        print(f"TypeError on '{alphaNumeric.__name__}(length)': length should be int but it receives '{length}' instead")
        raise
    except Exception as e:
        print(e)
        raise

def alphabeticalString(length: int):
    try:
        string = ""
        for _ in range(0, length):
            string += randchar()
        return string
    except TypeError:
        print(f"TypeError on '{alphabeticalString.__name__}(length)': length should be int but it receives '{length}' instead")
        raise
    except Exception as e:
        print(e)
        raise

def generateContent(maxLength: int):
    string = ""
    while len(string) < maxLength:
        content = choice([alphabeticalString, realnumber, integer, alphaNumeric])
        length = randint(MIN_LENGTH, MAX_LENGTH)
        string += f"{content(length)},"

    if len(string) > maxLength:
        diff = len(string) - maxLength
        temp = string[:-diff]
        string = temp

    if string[-1] == ',' or string[-1] == '.':
        temp = string
        string = temp[:-1] + ' '

    return string

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate text file with random string")
    parser.add_argument("-o", "--output", nargs="?", default="output.txt", type=str, help="Output filename")
    parser.add_argument("-p", "--process", nargs="?", default=1, type=int, help="Execute file in N process for faster execution")
    parser.add_argument("-s", "--size", nargs="?", default=500, type=int, help="Output file size in bytes")
    args = parser.parse_args()

    content = ""
    contentLength = math.ceil(args.size/args.process)
    processes = []

    with ProcessPoolExecutor() as executor:
        for _ in range(0, args.process):
            generate = executor.submit(generateContent, contentLength)
            processes.append(generate)

    for worker in processes:
        content += worker.result()

    # Create a file
    path = isFileExists(args.output)
    f = open(path, "w")
    f.write(content)
    f.close()
