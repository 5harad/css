"""
Solution for Exercise 4 of the python crash course

@author: Jongbin Jung
"""

# 1.
class BookReader:
    """Read a file and count the words"""
    def __init__(self, filename):
        self.filename = filename
        
    def count_words(self):
        """Count occurence of each word in the file's text"""
        self.words = {}  # initialize a dictionary        
        with open(self.filename, 'r') as f:
            for line in f:
                for word in line.lower().split():
                    try:
                        self.words[word] += 1
                    except KeyError:
                        self.words[word] = 1
        
        return self.words
        
bookReader = BookReader('two_cities.txt')
word_count = bookReader.count_words()  # assign the dictionary to word_count


# 2.
# Note that urllib2 is imported here to keep the scripts relevant to problem 2
# in one place. However, it's better practice (and highly recommended) to keep
# your imports collected at the very begining of every script.
import urllib2

class OnlineBookReader(BookReader):
    """Read a URL, save as file, and count the words"""
    def __init__(self, URL, filename='tmp'):  # set a default filename
        self.link = urllib2.urlopen(URL)  # open the url
        text = self.link.read()
        with open(filename, 'w') as f:  # open file to write on
            f.write(text)
        BookReader.__init__(self, filename)

obr = OnlineBookReader('https://goo.gl/fHIeOi')
online_word_count = obr.count_words()  # assign the dictionary to word_count