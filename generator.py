import argparse, math, re, sys
from concurrent.futures import ProcessPoolExecutor

from module.content import generateContent
from module.helper import isFileExists

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Generate text file with random string")
        parser.add_argument("-o", "--output", nargs="?", default="output.txt", type=str, help="Output filename")
        parser.add_argument("-p", "--process", nargs="?", default=1, type=int, help="Execute file using N process for faster execution")
        parser.add_argument("-s", "--size", type=int, help="Output file size in bytes", required=True)

        if len(sys.argv) == 1:
            parser.print_help()
            print("\n")

        args = parser.parse_args()

        if args.process > args.size: # Prevent redundant process
            args.process = args.size
        if args.size < 1:
            raise ValueError("Size should not less than 1")
        if args.process < 1:
            raise ValueError("Process should not less than 1")
        if not re.fullmatch(r"^[a-zA-Z](\w||[-./()\[\]{}])*", args.output):
            raise ValueError("Invalid filename format, filename should start with alphabet then continue with alphabet, number, or allowed symbol '[,],.,-,_,(,)'")

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
    except Exception as e:
        print(e)
        sys.exit(1)
