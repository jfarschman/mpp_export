# mpp_export

#### Table of Contents

1. [Overview](#overview)
2. [In a Nutshell](#Nutshell)
3. [Usage - How to Start](#usage)
    * [Install API Client](#install-api-tools)
    * [Environment Variables](#environment-variables)
    * [Exporting the Content](#exporting-the-content)
4. [Limitations - OS compatibility, etc.](#limitations)
5. [Contributors](#contributors)

## Overview
Tools for exporting from Metro Publisher's API.

## Nutshell
This is python for pulling the content from the metropublisher API and Writing
it out as a .csv.
`check_csv.py`
`put_articles.py`.

## Usage

### Install API Tools
The API client library tools are supplied by Vanguardistas and are
available here https://github.com/vanguardistas/van_api

```bash
git clone https://github.com/vanguardistas/van_api.git
./setup.py
```

### Environment Variables
So, I can check this code it I'm using environment variables and asking python
to grab these variables at run time. Generate an API key and if you want to mess
with locations, a geoname_user (http://api.geonames.org/).  The export these on
the CLI prior to running the commands:

export APIKEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export APISECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export APIID=xxx
export GEONAME_USER=yourusername

#### Exporting the content
`export_content_as_csv`
`export_locations_as_csv`
`export_sections_as_csv`

## Limitations
This was tested on Mac OSX only.

## Contributors
Jay Farschman - jfarschman@gmail.com
