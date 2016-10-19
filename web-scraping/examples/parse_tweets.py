#!/usr/bin/env python2
'''
Example for parsing json results from tweepy

Requires:
    pytz
        pip install pytz
'''

import sys
from datetime import datetime
import json
import pytz


def main():
    '''
    Main function
    '''

    # process stdin line-by-line
    for line in sys.stdin:
        line = line.rstrip('\n')

        # check for blank lines
        if line != '':
            try:
                tweet = json.loads(line)
            except:
                # print 'skipped non json entry'
                continue

            # make sure that the tweet has all required fields
            if 'user' in tweet and 'created_at' in tweet:

                time_zone = str(tweet['user']['time_zone'])

                # only process tweets where users have specified US time-zones
                if 'US' in time_zone:
                    time_zone = 'US/' + time_zone.split()[0]
                    clean_time = datetime.strptime(
                        tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
                    mytime = pytz.utc.localize(
                        clean_time).astimezone(pytz.timezone(time_zone))
                    print '\t'.join((mytime.strftime('%m/%d'),
                                     mytime.strftime('%H'),
                                     mytime.strftime('%M'),
                                     mytime.strftime('%Z')))

if __name__ == '__main__':
    main()
