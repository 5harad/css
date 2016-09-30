"""
Solution for Exercise 3 bonus question of the python crash course.

@author: Jongbin Jung
"""
import sys


def top_n(d, n=5):
    i = 1  # count to n
    for word in sorted(d, key=d.get, reverse=True):
        print word, d[word]
        if i == n:
            break
        i += 1

if __name__ == '__main__':
    n = int(sys.argv[1])  # n as first argument
    words = {}
    for line in sys.stdin:
        for word in line.lower().split():
            try:
                words[word] += 1
            except KeyError:
                words[word] = 1

    # call the top_n function
    top_n(words, n)
