# python-wrapper-script

`script.sh` is a small wrapper script to quickly bootstrap new projects in Python.

## Prerequisites

For this script to work, you need the following things:
- Python 3.*
- Both the script and the wrapper should have the same basename

## Dependencies

Simply add your packages in a `requirements.txt` file.
They will be installed or updated before each execution of the script.

## Environment variables

Any file starting with `.env` will be loaded in the environment before invoking the Python script.

A good practice is to split the variables in two files:
- `.env.shared` for any public variable (this file can be added to the source control)
- `.env.secret` for any private secret (this file SHOULD never be added to the source control)

## Command line arguments & stdin

Just execute the wrapper script appending any command line vrariable and piping any stdin content you want.
