#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests # (Zenodo)


"""
Create a "master list" (actually a dictionary) of data sources
Envisage that this will primarily be for testing/development

Parameters
----------
None

Returns
-------
dictionary
Keys are the data-source names,
Values are the data-source locations

Examples
--------
>>> master_dict = generate_test_master_dictionary()

"""
def generate_test_master_dictionary():
    return { 'leap-seconds': 'https://www.ietf.org/timezones/data/leap-seconds.list' }


"""
Convert a "master list" (actually a dictionary) of data sources to JSON
Upload the JSON to standard (hard-coded) external location(s)

Parameters
----------
master_dictionary : dictionary of data sources
Keys are the data-source names,
Values are the data-source locations

Returns
-------
...

Examples
--------
>>> ...

"""
def master_upload(master_dictionary):
    FAILED = False
    
    # Convert to JSON
    print(type(master_dictionary))
    master_JSON = json.dumps(master_dictionary)
    
    # Upload to MPC Website
    try:
        MPCMasterLocn = master_upload_to_MPCWebsite(master_JSON)
    except:
        print("Failed to upload to MPC website")
        FAILED = True
    
    # Upload to Zenodo
    try:
        ZenodoMasterLocn = master_upload_to_Zenodo(master_JSON)
    except:
        print("Failed to upload to Zenodo website")
        FAILED = True

    # Upload to Google Drive
    try:
        GoogleMasterLocn = master_upload_to_GoogleDrive(master_JSON)
    except:
        print("Failed to upload to Google website")
        FAILED = True

    # Return Master Locations
    return (False, [] )  if FAILED else (True, [MPCMasterLocn,ZenodoMasterLocn,GoogleMasterLocn])


"""
Upload a "master list" (in JSON format) to Zenodo
# http://developers.zenodo.org/#quickstart-upload

Parameters
----------
master_JSON :

Returns
-------
...

Examples
--------
>>> ...
    
"""
def master_upload_to_Zenodo(master_JSON, ACCESS_TOKEN):
    
    print("ACCESS_TOKEN" , ACCESS_TOKEN)
    
    # Check access works
    try:
        r = requests.get('https://zenodo.org/api/deposit/depositions',params={'access_token': ACCESS_TOKEN})
        assert r.status_code == 200
    except:
        print("Failed to get access")
    
    # Create empty upload
    try:
        headers = {"Content-Type": "application/json"}
        r = requests.post('https://zenodo.org/api/deposit/depositions',
                          params={'access_token': ACCESS_TOKEN}, json={}, headers=headers)
        assert r.status_code == 201
    except:
        print("Failed to create empty upload")

    # Upload data
    try:
        # Get the deposition id from the previous response
        deposition_id = r.json()['id']
        data = {'filename': 'MPCDataMaster.json'}
        files = {'file': master_JSON }
        r = requests.post('https://zenodo.org/api/deposit/depositions/%s/files' % deposition_id,
                          params={'access_token': ACCESS_TOKEN}, data=data, files=files)
        assert r.status_code == 201
    except:
        print("Failed to upload data")
        
    # Upload metadata
    try:
        data = {
            'metadata': {
                'title': 'MPC Master Data List',
                'upload_type': 'dataset',
                'description': 'List of data sources used/required by MPC packages',
                'creators': [{'name': 'Payne, Matthew','affiliation': 'MPC'}]
                }
            }
        r = requests.put('https://zenodo.org/api/deposit/depositions/%s' % deposition_id,
                         params={'access_token': ACCESS_TOKEN}, data=json.dumps(data), headers=headers)
        assert r.status_code == 200
    except:
        print("Failed to upload metadata")
    
    
    # Final Publish
    try:
        r = requests.post('https://zenodo.org/api/deposit/depositions/%s/actions/publish' % deposition_id,
                  params={'access_token': ACCESS_TOKEN} )
        assert r.status_code == 202
    except:
        print("Failed to do final publish")

    print(r.json())
    return r

"""
Upload a "master list" (in JSON format) to the MPC Website

Parameters
----------
master_JSON

Returns
-------
...

Examples
--------
>>> ...

"""
def master_upload_to_MPCWebsite(master_JSON):
    return True

"""
    Upload a "master list" (in JSON format) to Google-Drive
    # https://developers.google.com/drive/api/v3/about-sdk
    
    Parameters
    ----------
    master_JSON
    
    Returns
    -------
    ...
    
    Examples
    --------
    >>> ...
    
    """
def master_upload_to_GoogleDrive(master_JSON):
    return True
