"""Example module5"""

import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    if 'two' in line.split():
        print(line)
