# SuperProcessor

> the perfect wrapper for subprocess.run

## Goal

Write Shell commands in Python with ease. Simplify Scripting for All.

## Description 

This module is meant to ease use of `subprocess.run`,
minimizing and reducing all possible edge cases that
are prone to come with use of traditional `run()`.



## Dependencies

None! This module relies on zero external dependencies, 
making use of only the builtin module `subprocess`.

## Installation

Install either over Pypi with 

    pip3 install superprocessor
    
or over git-pip

    pip3 install git+https://github.com/samocorp/superprocessor.git
    

## Usage

This module is famous for the `cmd` function, which has a signature of 

    cmd(* args: str, ** kwargs) -> Tuple(stdout: str, stderr: Union[str, None])

As you can see, this function implements a Golang-style error handling, of returing
both the std output, error, and status code of the command in the shell.

If no error is encountered, the second value of the returned tuple is of NoneType.

Importing and using the function is easy.

    from superprocessor import cmd
    
    cmd('mkdir -p ', NEW_DIR_P, \
    '&& cd', NEW_DIR_P, \
    '&& npm install')
    
See [/examples](https://github.com/samocorp/superprocessor/tree/master/examples) for more use cases.


Since a tuple is returned, you have to unpack it for every call.

    # WRONG
    OUT = cmd(...)
    
    
    # RIGHT
    OUT, ERR, STATUS = cmd(...)
    
Although unrecommended, you might end up un-naming parts of it

     out, _, _ = cmd(...)

### Configurations

     
Create wickedly easy configuration overrides for example:

    # logging insightful clues to stdout
    # default: False
    cmd(..., log=True)
    # or environment SUPER_LOGS=TRUE     
     
     
     
Happy Scripting :-)
    
    
    
## Support

Please reach out to us for anything at

<thesamocorp@gmail.com> 

Create issues, fork and request merge requests, and don't be a stranger.

## License

This project is governed by the MIT License.

Copyright SamoCorp 2021.

All Rights Reserved.
