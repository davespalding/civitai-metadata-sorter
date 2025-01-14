# civitai-metadata-sorter

## General

This repo contains a personal tool for sorting metadata I store from CivitAI. Whenever I download a file from CivitAI (e.g. checkpoint or LoRA), I store some of the listed metadata to a local text file for handy access in case the file gets deleted from the website. To save time, I created this script for automating this task as keeping files alphabetically sorted by hand takes more and more time as these metadata files grow in size.

The data is sorted by filename of an entry. You can view an example of an input file on path `tests/res/`.

## Usage
You can type `python -m sort -h` on the root folder for instructions using this tool.

```
$ python -m sort -h
usage: CivitAI metadata file sorter. [-h] -f FILE [-b]

Sort metadata blocks from a CivitAI metadata text file.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to file.
  -b, --backup          Create backup of target file.
```

## License
This repo is under MIT license.