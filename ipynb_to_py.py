#!/usr/bin/env python3

import argparse
import glob
import json

def extract_code(afolder):
    for infile in glob.glob("./**/*.ipynb", recursive=True):
        outfile = infile.replace('.ipynb', '.py')
        with open(outfile, 'w') as out_f:
            with open(infile, encoding='utf-8') as in_f:
                print("Processing:", infile, 'into', outfile)
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
    parser.add_argument('--folder', action='store', dest='folder')
    args = parser.parse_args()
    afolder = args.folder
    extract_code(afolder)
      
    
