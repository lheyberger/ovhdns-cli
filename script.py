#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from os import environ


PUBLIC_VAR = environ.get('PUBLIC_VAR')
PRIVATE_VAR = environ.get('PRIVATE_VAR')


def main():
    print(f'Command line arguments: {sys.argv}')

    if not sys.stdin.isatty():
        print(f'First line from stdin: [{next(sys.stdin).strip()}]')

    print(PUBLIC_VAR, PRIVATE_VAR)


if __name__ == '__main__':
    main()
