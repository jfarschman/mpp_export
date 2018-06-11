#!/usr/bin/python
"""Export files to a CSV file.

"""

import sys
import csv
import json
import urllib
import os
import logging

import van_api

# Configuration
API_KEY     = os.environ["APIKEY"]
API_SECRET  = os.environ["APISECRET"]
INSTANCE_ID = os.environ["APIID"]


def get_all_items(api, start_url):
    """Return an iterator of all the items in a collection

    Pages through all available URLS
    """
    filename_list = []
    download_url_list = []

    result = api.GET(start_url)
    for items in result['items']:
        result2 = api.GET(items[0])
        filename_list.append(result2['filename'])
        download_url_list.append(result2['download_url'])
    return filename_list, download_url_list


def to_csv_value(in_file):
    """Convert file object from the API to dict of UTF-8 encoded bytes."""
    out_file = {}
    for k, v in in_file.items():
        # print k, v
        if v is None:
            v = u''
        elif isinstance(v, list):
            v = [unicode(i) for i in v]
            v = u'|'.join(v)
        elif not isinstance(v, basestring):
            v = unicode(v)
        out_file[k] = v.encode('utf-8')
    return out_file


def main():
    # setup logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

    # Get an API connection
    credentials = van_api.ClientCredentialsGrant(API_KEY, API_SECRET)
    api = van_api.API('api.metropublisher.com', credentials)

    fields = ['url', 'title']
    # page=2&rpp=2'
    start_url = '/{}/files?groups=image&fields={}&page=1&rpp=100'.format(INSTANCE_ID, '-'.join(fields))
    # print url

    csv_file = None
    count = 0

    download_filename, download_url = get_all_items(api, start_url)

    # create images folder in the current directory
    try:
        if not os.path.exists('images'):
            os.makedirs('images')
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

    f = open('all_files.csv', 'wb')
    f.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)

    fieldnames = ['Filename', 'Download URL']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for filename, url in zip(download_filename, download_url):
        count += 1

        # Download the jpg image file
        with open('./images/' + filename, 'wb') as handler:
            api.GET(url, handler)
            bytes_written = handler.tell()
            logging.info("Downloaded " +
                         filename + " %s bytes" % bytes_written)

        writer.writerow({'Filename': filename.encode('utf8'), 'Download URL': url.encode('utf8')})

    logging.info('Exported {} file'.format(count))
    return 0


if __name__ == '__main__':
    sys.exit(main())
