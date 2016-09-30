# save this function to a file named module3.py
def speak():
    """Make module 3 say something"""
    print 'My __name__ is', __name__
    

if __name__ == '__main__':
    speak()
    print 'You\'ve executed me!'