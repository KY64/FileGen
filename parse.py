import argparse, re

def isAlphabet(string: str):
    return re.fullmatch(r"[a-zA-Z]+", string)

def isAlphanumeric(string: str):
    return re.fullmatch(r"\s*\w+\s*", string)

def isFloat(string: str):
    return re.fullmatch(r"\d+\.\d+", string)

def isNumber(string: str):
    return re.fullmatch(r"\d+", string)

parser = argparse.ArgumentParser(description="Parse file that has generated from generator.py")
parser.add_argument("file", metavar="file", type=str, help="File that needs to be parsed")
args = parser.parse_args()

file = open(args.file, "r").read()

for value in file.split(','):
    contentType = "Unrecognized"

    if isNumber(value):
        contentType = "integer"
    elif isFloat(value):
        contentType = "real numbers"
    elif isAlphabet(value):
        contentType = "alphabetical strings"
    elif isAlphanumeric(value):
        value = value.strip()
        contentType = "alphanumeric"
    print(value, '-', contentType)
