#!/usr/bin/env python2
'''
Example using selenium to wait for load

Requires:
    selenium
        pip install selenium

Note: For  Firefox 47.0+ you'll need to install the Marionette webdriver, see:
    https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def main():
    '''
    Main function
    '''
    browser = webdriver.Firefox()
    browser.get('http://www.theguardian.com/us')

    # wait for at least one 'fc-container__inner' to load and return a list of
    #   all fc-container__inner to variable containers
    #   wait maximum MAX_WAIT seconds, and exit with message on timeout
    MAX_WAIT = 10
    try:
        containers = WebDriverWait(browser, MAX_WAIT).until(
            EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, 'fc-container__inner')))
    except TimeoutException:
        print 'I timed out!'

    for container in containers:
        # match the headlines container
        if container.text.split()[0].lower() == 'headlines':
            for headline in (container
                             .find_elements_by_class_name(
                                 'js-headline-text')):
                print headline.text
                headline.click()  # open the headline

                try:
                    WebDriverWait(browser, MAX_WAIT).until(
                        EC.presence_of_element_located(
                                (By.CLASS_NAME, 'commentcount2'))).click()

                    authors = WebDriverWait(browser, MAX_WAIT).until(
                        EC.presence_of_all_elements_located(
                                (By.CLASS_NAME, 'd-comment__author')))
                except TimeoutException:
                    print 'I timed out!'

                contents = browser.find_elements_by_class_name(
                    'd-comment__content')

                for author, content in zip(authors, contents):
                    comment = content.find_element_by_tag_name('p')
                    print author.text, ':', comment.text

                # we can do more crazy-looking stuff to try and go back and
                #   open the next headline, get comments from that, etc.
                #   but we'll stop here for today ...
                break  # iteration over headlinse
            break  # iteration over containers

if __name__ == '__main__':
    main()
