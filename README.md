<div align="center">
	<h1>FileGen</h1>
	<br />
	<image src="logo.svg" width=150 />
	<br />
	<br />
</div>

Text file generator program built with Python. Use [generator.py](./generator.py) to generate content containing alphanumeric, alphabetical string, integer and real number. The example output can be seen on [output.txt](./output.txt)

## Requirement

- Python 3.7+

## Usage

### Generate Text File

To generate text file, execute **generator.py** such as the following example:

```sh
python generator.py --size 500
```

The command above will generate text file named **output.txt** with size of 500 bytes. You can specify `size` argument as small as 1 byte and as large as you need.

For faster execution, you can add `process` argument such as the following example:

```sh
python generator.py --size 10485760 --process 4
```

The command above will generate text file with size of 10 megabytes using 4 processes. It means the program will reserve 4 cores of your CPU to generate file so make sure you define this argument based on amount of available CPU core.

**Available command**

```sh
$ python generator.py 
usage: generator.py [-h] [-o [OUTPUT]] [-p [PROCESS]] -s SIZE

Generate text file with random string

optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUT], --output [OUTPUT]
                        Output filename
  -p [PROCESS], --process [PROCESS]
                        Execute file using N process for faster execution
  -s SIZE, --size SIZE  Output file size in bytes
```

### Parse Output From generator.py

To parse the output from **generator.py**, execute **parse.py** such as the following example:

```sh
python parse.py output.txt
```

The command above will parse **output.txt** file and the result would be:

```
H6Mj7rKRsWx5KUx149B48ClE6A - alphanumeric
3287614992 - integer
6Fe0y08d691D82A - alphanumeric
7973164013.302224 - real numbers
5678392141.792594 - real numbers
8257352750 - integer
2884305332.742737 - real numbers
J893UWh08O9lH59ftn731q - alphanumeric
b40l91 - alphanumeric
1032071840 - integer
O1Y0HH7628sdZi05295683V1jSc - alphanumeric
txxbhLdqnQJkioewGKHhrdhMziklInpMqEaIYeuL - alphabetical strings
837317p24E6yby6d72O3w6j321jz378E - alphanumeric
3627597279 - integer
4vbh8PHgfuR45o - alphanumeric
```

**Available command**

```sh
$ python parse.py 
usage: parse.py [-h] file

Parse file that has generated from generator.py

positional arguments:
  file        File that needs to be parsed

optional arguments:
  -h, --help  show this help message and exit
```

## Testing

The test files are placed in **test** directory, you can run the test using the following command:

```sh
git clone https://github.com/KY64/FileGen.git
cd FileGen/
python -m unittest -v
```

## Project Structure

```sh
.
├── LICENSE
├── README.md
├── generator.py
├── module
│   ├── __init__.py
│   ├── content.py
│   └── helper.py
├── output.txt
├── parse.py
└── test
    ├── __init__.py
    ├── test_alphaNumeric.py
    ├── test_alphabeticalString.py
    ├── test_appendwhitespace.py
    ├── test_generateContent.py
    ├── test_helperModule.py
    ├── test_integer.py
    ├── test_randchar.py
    └── test_realnumber.py
```

- **generator.py**: a program to generate file
- **module**: local module
- **content.py**: module containing content-related function (e.g. generate real number, generate alphanumeric)
- **helper.py**: module containing function to ease development (e.g. trim redundant string, validate content, etc.)
- **output.txt**: example output from generator.py
- **parse.py**: a program to parse output file from generator.py
- **test**: directory containing test files

### Attribution

- Logo by [freepik](https://www.flaticon.com/authors/freepik)