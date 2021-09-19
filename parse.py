import argparse, os, re, sys

from module.helper import isAlphabet, isAlphanumeric, isFloat, isNumber

if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser(description="Parse file that has generated from generator.py")
        parser.add_argument("file", metavar="file", type=str, help="File that needs to be parsed")

        if len(sys.argv) == 1:
            parser.print_help()
            print("\n")

        args = parser.parse_args()

        if not re.fullmatch(r"^[a-zA-Z](\w||[-./()\[\]{}])*", args.file):
            raise ValueError("Invalid filename format, filename should start with alphabet then continue with alphabet, number, or allowed symbol '[,],.,-,_,(,)'")
        if not os.path.exists(args.file):
            raise FileNotFoundError("File not found")

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
    except Exception as e:
        print(e)
