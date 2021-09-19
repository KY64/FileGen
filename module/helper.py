import os, re

def fitContent(string: str, maxLength: int):
    if len(string) > maxLength:
        diff = len(string) - maxLength
        temp = string[:-diff]
        string = temp

    if string[-1] == ',' or string[-1] == '.':
        temp = string
        string = temp[:-1] + ' '

    return string

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
