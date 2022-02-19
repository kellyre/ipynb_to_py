#!/usr/bin/env python3

import argparse
import glob
import json
from os.path import exists, join
import sys

def extract_code(folder, overwrite, recurse, suffix):
'''Read in ipynb files from a directory or a directory tree.
For each file, read just the code portions of the files and
write them back to new ".py" files. Without the overwrite flag
'''
    glob_string = join(folder, "*.ipynb")
    if recurse:
        glob_string = join(folder, "**", "*.ipynb")
    for infile in glob.glob(glob_string, recursive=recurse):
        outfile = infile.replace('.ipynb', suffix)
        if not overwrite and exists(outfile):
            print(f"Refusing to overwrite: {outfile}")
            continue
        with open(outfile, 'w') as out_f:
            with open(infile, encoding='utf-8') as in_f:
                print(f"Processing: {infile} into {outfile}")
                try:
                    data = json.load(in_f)
                    for acell in data['cells']:
                        cell_type = acell['cell_type']
                        out_f.write(f"\n\n### {cell_type}\n")
                        src = acell['source']
                        for line in src:
                            if cell_type=='code':
                                out_f.write(f"{line}")
                            else:
                                out_f.write(f"# {line}")
                except json.decoder.JSONDecodeError as e:
                    print(f"JSON parsing error: {e}")
                except Exception as e:
                    print(f"Got error: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract code from ipynb files')
    parser.add_argument('--folder', '-f', dest='folder', action='store',
                        help='folder to look for ipynb files')
    parser.add_argument('--overwrite', '-o', dest='overwrite', action='store_true',
                        help='overwrite files if they exist (default: False)')
    parser.add_argument('--recurse', '-r', dest='recurse', action='store_true',
                        help='recurse into subdirectories looking for files (default: False)')
    parser.add_argument('--suffix', '-s', dest='suffix', action='store',
                        help='suffix to apply to new files (default: .py)')
    parser.set_defaults(overwrite=False, recurse=False, suffix='.py')
    args = parser.parse_args()

    extract_code(
        folder=args.folder,
        overwrite=args.overwrite,
        recurse=args.recurse,
        suffix=args.suffix
    )
      
    
