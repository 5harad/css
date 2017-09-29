#!/usr/bin/env python2
"""Example mapper module for counting words via map-reduce.

This file is saved as wc_mapper.py with execute permission
(chmod +x wc_mapper.py)"""

import sys


def main():
    """Take lines from stdin and emit each word with count 1.

    This is for illustration purposes, treating any string separated by
    whitespace as a 'word'. Additional cleaning (e.g., removing punctuation)
    could be added if necessary."""
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            print(word + '\t' + '1')


if __name__ == "__main__":
    main()
