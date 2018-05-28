#!/usr/bin/python
"""Export files to a CSV file.
"""

import sys
import csv
import json
import urllib
import os
import logging
import tempfile
from pprint import pprint

import van_api

# Configuration
API_KEY      = os.environ["APIKEY"]
API_SECRET   = os.environ["APISECRET"]
INSTANCE_ID  = os.environ["APIID"]

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

# Get an API connection
credentials = van_api.ClientCredentialsGrant(API_KEY, API_SECRET)
api = van_api.API('api.metropublisher.com', credentials)
start_url = '/{}'.format(INSTANCE_ID)

# get list of files
logging.info("Getting Files")
result = api.GET(start_url + '/files')
pprint(result)

# get file metadata
url_to_first_file = result['items'][0][0]
logging.info("Getting Metadata of the first file from %s" % url_to_first_file)
result = api.GET(url_to_first_file)
pprint(result)

# Download data
logging.info("Downloading file data to a filename")
with open('afile', 'wb') as handler:
    api.GET(result['download_url'], handler)
    bytes_written = handler.tell()
logging.info("Downloaded %s bytes" % bytes_written)
