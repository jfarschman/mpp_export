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
logging.info("Getting top-level catalog of resources in the instance/site.")
result = api.GET(start_url)
pprint(result)

logging.info("Getting top-level list of sections")
#result = api.GET('/282/sections?fields=title-urlname-url')
result = api.GET(start_url + '/sections?fields=title-urlname-url')
pprint(result)
