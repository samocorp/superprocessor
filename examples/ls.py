
from superprocessor import cmd

files, _ = cmd(
    'ls'
)

for f in files.strip('\n').split('\n'):
    print(f'found file: {f}')
