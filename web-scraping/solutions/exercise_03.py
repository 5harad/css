#!/usr/bin/env python2
'''
Web scraping with access to json api using requests

Requires
    requests(http://docs.python-requests.org/)
        pip install requests

    This will collect and print
    VIN, year, trim, mileage, price
    for all used cars available within 50 miles of specified
    zipcode, make, and model

@author: Jongbin Jung (jongbin at stanford edu)
'''

import requests


def main():
    '''
    Main function
    '''
    # set parameters
    make = 'Honda'
    model = 'Accord'
    params = {
        'zipcode': '94305',
        'range': '50',
        'make': make,
        'model': model,
    }

    # specify the items we're interested in
    keys = ['vin', 'year', 'trim', 'mileage', 'price']

    # this is a place holder for the url to the api that you'll
    # find during the workshop!
    base_url = '/url/to/api'

    # request json file with GET
    cars = requests.get(base_url, params=params).json()

    # print tsv of columns
    for car in cars['inventory']:
        print '\t'.join([car[key] for key in keys])

    print 'Collected data for', cars['totalCount'], make, model, 'listings'

if __name__ == '__main__':
    main()
