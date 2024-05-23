Environment Variables and Command Line Arguments
---------------------------------------------------------------------
In Python, you can handle environment variables and command line arguments using the `os` and `sys` modules, respectively. Here’s an overview and examples of how to work with both.

Environment Variables
---------------------
Environment variables are external variables that can affect the way running processes will behave on a computer. They can be accessed and modified in Python using the `os module`.

Accessing Environment Variables

You can use `os.getenv` to get the value of an environment variable.

Example:


`import os

 print(os.getenv("password"))`


Command Line Arguments
----------------------

Command line arguments are inputs passed to a script when it is executed. These can be accessed using the `sys` module.

Accessing Command Line Arguments
You can access command line arguments using `sys.argv`. The first element in this list, `sys.argv[0]`, is the name of the script.



