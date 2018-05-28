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

If you get an error like the one below you've failed to export your environment
variables.
```
Traceback (most recent call last):
  File "./download_one.py", line 18, in <module>
    API_KEY      = os.environ["APIKEY"]
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/UserDict.py", line 23, in __getitem__
    raise KeyError(key)
KeyError: 'APIKEY'
```

#### Exporting the content
This section list the commands available to GET resources from the API. They are
briefly described:

`overview.py`             - Shows the catalog of resource types and sections as
                            json.

`export_content_as_csv`   - Capture all content (articles/reviews) as a csv to
                            stdout.

`export_events_as_csv`    - Capture all events as a csv to stdout.

`export_files_as_csv`     - Capture all file metadata as a csv to stdout. this
                            output is used to pull the actual files.

`export_locations_as_csv` - Capture all locations as a csv to stdout.

`export_tag_as_csv`       - Capture all tags as a csv to stdout. Tags are attached
                            to content to create an association between a author
                            place, idea. Clicking a tag will bring up a list of
                            other similarly tagged content.

`export_sections_as_csv`  - Capture sections


## Limitations
This was tested on Mac OSX only.

## Contributors
Jay Farschman - jfarschman@gmail.com
