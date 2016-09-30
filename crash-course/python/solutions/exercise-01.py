"""
Solution for Exercise 1 of the python crash course

@author: Jongbin Jung
"""

# 1. 
s = '"double quotes" and \'single quotes\' are equally acceptable in pyton'
# or equivalently:
s = "\"double quotes\" and 'single quotes' are equally acceptable in python"


# 2. 
s.count('t')


# 3. 
s = s.replace('"', '_')
s = s.replace("'", '_')


# 4.
words = s.split()


# 5.
len(s)
len(words)


# 6.
','.join(words)