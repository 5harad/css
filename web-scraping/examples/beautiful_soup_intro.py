#!/usr/bin/env python2
'''
Intro to BeautifulSoup

Requires:
    BeautifulSoup(http://www.crummy.com/software/BeautifulSoup)
        pip install beautifulsoup4
    requests(http://docs.python-requests.org/)
        pip install requests
'''

from bs4 import BeautifulSoup
import requests


def main():
    '''
    Main function
    '''
    web_page = requests.get('http://www.crummy.com/software/BeautifulSoup/')

    soup = BeautifulSoup(web_page.content)

    # Read the first H1 tag (usually the 1st-level header, unless you're
    # dealing with a rogue  web designer)
    print soup.h1

    # return the first link (an a tag), get its address (href property)
    print soup.a
    soup.a.get('href')

    # find all the links in the document
    soup.a.find_all('a')

    # get all the link addresses using a for loop
    for link in soup.a.find_all('a'):
        print link.get('href')

    # or make a list of the addresses with list comprehension
    addresses = [link.get('href') for link in soup.a.find_all('a')]
    print addresses

if __name__ == '__main__':
    main()
