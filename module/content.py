from random import choice, randint, uniform
from .helper import fitContent

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
    try:
        if maxLength < 1:
            return

        string = ""
        while len(string) < maxLength:
            content = choice([alphabeticalString, realnumber, integer, alphaNumeric])
            length = randint(MIN_LENGTH, MAX_LENGTH)
            string += f"{content(length)},"

        return fitContent(string, maxLength)
    except Exception as e:
        print(e)
        raise
