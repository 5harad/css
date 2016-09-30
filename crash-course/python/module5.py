# save this code to a file named module5.py
import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    if 'two' in line.split():
        print line
