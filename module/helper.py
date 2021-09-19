import os, re

def fitContent(string: str, maxLength: int):
    try:
        if not isinstance(string, str):
            raise TypeError("string should has str type")
        if not isinstance(maxLength, int):
            raise TypeError("length should has integer type")
        if maxLength < 1:
            raise ValueError("length should not less than 1")
        if len(string) > maxLength:
            diff = len(string) - maxLength
            temp = string[:-diff]
            string = temp

        if string[-1] == ',' or string[-1] == '.':
            temp = string
            string = temp[:-1] + ' '

        return string
    except Exception as e:
        print(e)
        raise

def isAlphabet(string: str):
    return re.fullmatch(r"[a-zA-Z]+", string)

def isAlphanumeric(string: str):
    if not re.search(r"\d+", string):
        raise ValueError("Alphanumeric should contains number and alphabet but number is missing")
    if not re.search(r"[a-zA-Z]+", string):
        raise ValueError("Alphanumeric should contains number and alphabet but alphabet is missing")
    return re.fullmatch(r"\s+\w+\s+", string)

def isFloat(string: str):
    return re.fullmatch(r"\d+\.\d+", string)

def isNumber(string: str):
    return re.fullmatch(r"\d+", string)

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
