#!/usr/bin/env python2
'''
Building URLs from parameters

Requires:
    requests(http://docs.python-requests.org/)
        pip install requests
'''

import requests


def main():
    '''
    Main function
    '''
    base_url = 'http://www.imdb.com/search/title'
    params = {'genres': 'action', 'sort': 'moviemeter,asc'}

    page = requests.get(base_url, params=params)
    print page.url

if __name__ == '__main__':
    main()
