#!/usr/bin/env python2
'''
Example of using tweepy

Requires:
    tweepy
        pip install tweepy
'''

import datetime
import sys
import argparse
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


class TimedListener(StreamListener):
    '''
    A StreamListener that's timed (in hours)

    Initiate with the time to run (default 1 hour)
    '''
    starttime = datetime.datetime.now()

    def __init__(self, runfor=1):
        StreamListener.__init__()
        self.starttime = datetime.datetime.now()
        self.runfor = runfor

    def on_data(self, tweet):
        print tweet
        if (datetime.datetime.now() - self.starttime >
                datetime.timedelta(hours=self.runfor)):
            print 'Total run time:', datetime.datetime.now() - self.starttime
            sys.exit()

    def on_error(self, status):
        print status


def main():
    '''
    Main function
    '''
    # help strings
    help_keyfile = '''\
    file with user credentials, formated exactly as
    api_key value_of_api_key
    api_secret value_of_api_secret
    token value_of_token
    token_secret value_of_token_secret\
    where the value_* are all replaced with actual values.
    See: https://apps.twitter.com/
    to create you own credentials.'''

    # set up the argument parser
    parser = argparse.ArgumentParser(
        description='Fetch data with Twitter Streaming API')
    parser.add_argument('--keyfile', help=help_keyfile, required=True)
    parser.add_argument('--filter', metavar='W', nargs='*',
                        help='space-separated list of words;'
                             'tweets that match any word in list are returned')
    parser.add_argument('--runfor', metavar='H', type=int,
                        help='duration to run script, in hours (default 1)',
                        default=1)
    args = parser.parse_args()

    # read twitter app credentials from provided file
    creds = {}
    for line in open(args.keyfile, 'r'):
        key, value = line.rstrip().split()
        creds[key] = value

    # set up authentication
    auth = OAuthHandler(creds['api_key'], creds['api_secret'])
    auth.set_access_token(creds['token'], creds['token_secret'])

    # set up stream
    twitter_stream = Stream(auth, TimedListener())

    if args.filter:
        # track specific tweets
        twitter_stream.filter(track=args.filter)
    else:
        # get random sample of tweets
        twitter_stream.sample()

if __name__ == '__main__':
    main()
