# pagelabels
Python library to manipulate PDF page labels

## Addpagelabels utility
### Installation
#### Dependencies
Install **pip** if you don't have it already:
```bash
$ sudo apt install python3-pip
```
Install [**pdfrw**](https://github.com/pmaupin/pdfrw):
```
$ pip3 install pdfrw
```
#### The script
```
$ git clone https://github.com/lovasoa/pagelabels-py.git
```
### How to use
Get to the directory where you cloned the script:
```
$ cd pagelabels-py
```

#### Add a new page index to the PDF
This adds a new index to the file `/tmp/test.pdf`,
without deleting the ones that may already exist.
The new index will take effect from the 1st page of the PDF,
will be composed of uppercase roman numerals, preceded by the string "Intro ",
and starting from "V".

Page numbers will be: "Intro V", "Intro VI", "Intro VII", ...
```
$ ./addpagelabels.py --startpage 1 --type "roman uppercase" --prefix "Intro " --firstpagenum 5 /tmp/test.pdf
```

#### Print usage info
```
$ ./addpagelabels.py -h
```

This should print:
```
usage: addpagelabels.py [-h] [--delete] [--startpage STARTPAGE]
                        [--type {letters lowercase,roman lowercase,letters uppercase,arabic,roman uppercase}]
                        [--prefix PREFIX] [--firstpagenum FIRSTPAGENUM]
                        file.pdf

Add page labels to a PDF file

positional arguments:
  file.pdf              the PDF file to edit

optional arguments:
  -h, --help            show this help message and exit
  --delete              delete the existing page labels
  --startpage STARTPAGE, -s STARTPAGE
                        the index (starting from 1) of the page of the PDF
                        where the labels will start
  --type {letters lowercase,roman lowercase,letters uppercase,arabic,roman uppercase}, -t {letters lowercase,roman lowercase,letters uppercase,arabic,roman uppercase}
                        type of numbers: arabic = 1, 2, 3, roman = i, ii, iii,
                        iv, letters = a, b, c
  --prefix PREFIX, -p PREFIX
                        prefix to the page labels
  --firstpagenum FIRSTPAGENUM, -f FIRSTPAGENUM
                        number to attribute to the first page of this index
```

#### Delete existing page labels from a PDF
```
$ ./addpagelabels.py --delete
```

