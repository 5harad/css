#!/usr/bin/env python2
'''
Web scraping script using requests and bs4

Requires:
    BeautifulSoup(http://www.crummy.com/software/BeautifulSoup)
        pip install beautifulsoup4
    requests(http://docs.python-requests.org/)
        pip install requests

    This will collect and print
    {Movie Title}   {Actor Name}    {Character Name}
    for the cast in each of the top 3 movies in the IMDb Top 250 list
    (http://www.imdb.com/chart/top?ref_=nv_ch_250_4)

    Script in its current state collects top 3 to save time during demo.
    This can be easily modified to collect top n

@author: Jongbin Jung (jongbin at stanford edu)
'''

from time import sleep
from bs4 import BeautifulSoup, SoupStrainer
import requests


def clean_text(text):
    '''
    Removes white-spaces before, after, and between characters

    :param text: the string to remove clean
    :return: a 'cleaned' string with no more than one white space between
    characters
    '''
    return ' '.join(text.split())


def get_cast_from_link(movie_link, movie_title=''):
    '''
    Go to the IMDb Movie page in link, and find the cast overview list.
    Prints tab-separated movie_title, actor_name, and character_played to
    stdout as a result. Nothing returned

    :param movie_link: string of the link to IMDb movie page
    :return: void
    '''
    movie_page = requests.get(movie_link)

    # Use SoupStrainer to strain the cast_list table from the movie_page
    # This can save some time in bigger scraping projects
    cast_strainer = SoupStrainer('table', class_='cast_list')
    movie_soup = BeautifulSoup(movie_page.content, parse_only=cast_strainer)

    # Iterate through rows and extract the name and character
    # Remember that some rows might not be a row of interest (e.g., a blank
    # row for spacing the layout). Therefore, we need to use a try-except
    # block to make sure we capture only the rows we want, without python
    # complaining.
    for row in movie_soup.find_all('tr'):
        try:
            actor = clean_text(row.find(itemprop='name').text)
            character = clean_text(row.find(class_='character').text)

            print '\t'.join([movie_title, actor, character])

        except AttributeError:
            pass


def main():
    '''
    Main function
    '''
    # Use requests.get('url') to load the page you want
    url = 'http://www.imdb.com/chart/top?ref_=nv_ch_250_4'
    web_page = requests.get(url)

    # Prepare the SoupStrainer to strain just the tbody containing the
    # list of Top 250 Movies
    list_strainer = SoupStrainer('tbody', class_='lister-list')

    # Parse the html content of the web page with BeautifulSoup
    soup = BeautifulSoup(web_page.content, parse_only=list_strainer)

    # Generate a list of the 'Rank & Title' column of each row and iterate
    # limit the list to the first 3 results
    movie_list = soup.find_all('td', class_='titleColumn', limit=3)

    for movie in movie_list:
        # remember to be nice, and sleep a while between requests!
        sleep(3)

        # There's only one <a> tag in each movie item, which contains the
        # Movie Title
        movie_title = movie.a.text

        # get the link to the movie's own IMDb page, and jump over
        link = 'http://imdb.com' + movie.a.get('href')

        get_cast_from_link(link, movie_title)

if __name__ == '__main__':
    main()
