#!/usr/bin/env python2
'''
Example for collecting cast from a movie on IMDb

Requires:
    BeautifulSoup(http://www.crummy.com/software/BeautifulSoup)
        pip install beautifulsoup4
    requests(http://docs.python-requests.org/)
        pip install requests
'''

from bs4 import BeautifulSoup
import requests


def clean_text(text):
    '''
    Removes white-spaces before, after, and between characters

    :param text: the string to remove clean
    :return: a 'cleaned' string with no more than one white space between
    characters
    '''
    return ' '.join(text.split())


def main():
    '''
    Go to the IMDb Movie page in link, and find the cast overview list.

    Prints tab-separated movie_title, actor_name, and character_played to
    stdout as a result.
    '''
    link = 'http://www.imdb.com/title/tt0111161/?ref_=nv_sr_1'
    movie_page = requests.get(link)

    # Strain the cast_list table from the movie_page
    soup = BeautifulSoup(movie_page.content)

    # Iterate through rows and extract the name and character
    # Remember that some rows might not be a row of interest (e.g., a blank
    # row for spacing the layout). Therefore, we need to use a try-except
    # block to make sure we capture only the rows we want, without python
    # complaining.
    for row in soup.find('table', class_='cast_list').find_all('tr'):
        try:
            actor = clean_text(row.find(itemprop='name').text)
            character = clean_text(row.find(class_='character').text)

            print '\t'.join([actor, character])

        except AttributeError:
            pass

if __name__ == '__main__':
    main()
