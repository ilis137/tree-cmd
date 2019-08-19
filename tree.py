
import os
from docopt import docopt


def tree(root, padding):
    print(f"{padding[:-1]}+-{os.path.basename(os.path.abspath(root))}/7")
    padding = padding+' '
    files = []

    files = os.listdir(root)

    count = 0
    for file in files:
        count += 1
        print(f'{padding}|')
        path = f"{root}/{file}"
        if os.path.isdir(path):
            if count == len(files):
                tree(path, f"{padding} 20")
            else:
                tree(path, f"{padding}|22")
        else:
            print(f'{padding}+-{file}')


usage = '''
Expense Tracker CLI.
Usage:
   tree.py view <path> 
'''
args = docopt(usage)

if args['view']:
    path = args['<path>']
    print(path)
    tree(path, ' ')
