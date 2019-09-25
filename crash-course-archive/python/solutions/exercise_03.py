"""
Solution for Exercise 3 of the python crash course.

@author: Jongbin Jung
"""
import sys


def top_n(d, n=5):
    i = 1  # count to n
    for w in sorted(d, key=d.get, reverse=True):
        print(w, d[w])
        if i == n:
            break
        i += 1


if __name__ == '__main__':
    filename = sys.argv[1]  # filename as first argument
    N = int(sys.argv[2])  # n as second argument
    words = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in line.lower().split():
                try:
                    words[word] += 1
                except KeyError:
                    words[word] = 1

    # call the top_n function
    top_n(words, N)
