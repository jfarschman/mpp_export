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
API_KEY      = os.environ["APIKEY"]
API_SECRET   = os.environ["APISECRET"]
INSTANCE_ID  = os.environ["APIID"]

def get_all_items(api, start_url):
    """Return an iterator of all the items in a collection

    Pages through all available URLS
    """
    result = api.GET(start_url)
    page = 1
    while True:
        items = result['items']
        logging.info('got page {} ({} items), processing...'.format(page, len(items)))
        page += 1
        for i in items:
            yield i
        next_url = result.get('next')
        if not next_url:
            break
        if '?' not in next_url:
            next_url = start_url.split('?')[0] + '?' + next_url
        result = api.GET(next_url)

def to_csv_value(in_file):
    """Convert file object from the API to dict of UTF-8 encoded bytes."""
    out_file = {}
    for k, v in in_file.items():
        #print k, v
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
    start_url = '/{}/files?groups=image&fields={}&rpp=100'.format(INSTANCE_ID, '-'.join(fields))

    csv_file = None
    count = 0

    for download_url, filename in get_all_items(api, start_url):
        count += 1
        # get full file info
        file = api.GET(download_url)

        # cast everything to a string
        file = to_csv_value(file)
        if csv_file is None:

            # create our csv file writer if none already exists
            fieldnames = sorted(file.keys())
            print filename
            #fieldnames = 'fileation_uuid'
            csv_file = csv.DictWriter(sys.stdout, fieldnames)
            # write headers
            headers = dict([(k, k) for k in file])
            csv_file.writerow(headers)
        # write out one line of the CSV
        csv_file.writerow(file)
    logging.info('Exported {} files'.format(count))
    return 0

if __name__ == '__main__':
    sys.exit(main())
