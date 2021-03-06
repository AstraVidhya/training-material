#!/usr/bin/env python

import sys


def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        sys.stderr.write('### error: no input file specified\n')
        return 1
    try:
        in_file = open(file_name)
        with in_file:
            for line in in_file:
                print('|{0}|'.format(line.rstrip('\r\n')))
    except IOError as e:
        sys.stderr.write("### I/O error on '{0}': {1}".format(e.filename,
                                                              e.strerror))
        return 2
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
