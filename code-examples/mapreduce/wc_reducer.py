#!/usr/bin/env python2
"""Example reducer module for counting words via map-reduce.

This file is saved as wc_reducer.py with execute permission 
(chmod +x wc_reducer.py)"""

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(lines):
    """Returns generator over each line of lines as a list split by tabs."""
    for line in lines:
        yield line.rstrip().split('\t', 1)


def main():
    """Take lines from stdin and print the sum in each group of words."""
    data = read_mapper_output(sys.stdin)
    for word, group in groupby(data, itemgetter(0)):
        total_count = sum([int(count) for _, count in group])
        print word + '\t' + str(total_count)

if __name__ == "__main__":
    main()
