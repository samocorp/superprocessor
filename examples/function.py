
from superprocessor import cmd

print(cmd(
    'function foo { echo "Hello $1\n" ; } ; foo "jonas" ; '
))