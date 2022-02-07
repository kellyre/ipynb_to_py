# ipynb_to_py

Simple script takes a folder and recursively finds all ipynb files. For each ipynb file that it finds, it creates a Python script with the same name and extracts all the code blocks to that file.

usage: ipynb_to_py.py [-h] [--folder FOLDER] [--overwrite] [--recurse] [--suffix SUFFIX]

Extract code from ipynb files

optional arguments:
  -h, --help            show this help message and exit
  --folder FOLDER, -f FOLDER
                        folder to look for ipynb files
  --overwrite, -o       overwrite files if they exist (default: False)
  --recurse, -r         recurse into subdirectories looking for files (default: False)
  --suffix SUFFIX, -s SUFFIX
                        suffix to apply to new files (default: .py)


