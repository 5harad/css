#!/usr/bin/env python2
'''
Web scraping script using requests and bs4

Requires
    BeautifulSoup(http://www.crummy.com/software/BeautifulSoup)
        pip install beautifulsoup4
    requests(http://docs.python-requests.org/)
        pip install requests

    This will collect and print
    {Movie Title}   {Released Year}    {Gross Box Office Income}
    for the each of the top 250 movies in the IMDb Top comedy

@author: Jongbin Jung (jongbin at stanford edu)
'''

from time import sleep
from bs4 import BeautifulSoup
import requests


def main():
    '''
    Main function
    '''
    base_url = 'http://www.imdb.com/search/title'

    # loop over the pages with the start parameter
    for start in range(1, 250, 50):
        # Use requests to set URL with params and load
        params = {'genres': 'comedy',
                  'sort': 'boxoffice_gross_us',
                  'start': start}
        sleep(3)  # sleep before calls
        page = requests.get(base_url, params=params)

        # Parse the html content of the web page with BeautifulSoup
        soup = BeautifulSoup(page.content)

        for movie in soup.find_all('div', class_='lister-item-content'):
            try:
                title = movie.find('h3', class_='lister-item-header').a.text
                year = movie.find('span', class_='lister-item-year').text
                gross = (movie.find('span', text='Gross:')
                         .find_next_sibling('span').get('data-value'))

                print title, year, gross
            except AttributeError:
                pass

if __name__ == '__main__':
    main()
