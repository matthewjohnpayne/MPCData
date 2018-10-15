# mpcdata/tests/test_query.py
# import pytest

# Third-party imports
import os

# Import the specific package/module/function we are testing
import mpcdata.query as query


def test_failureDict():
    """
    Is failureDict present and populated as desired?
    """
    assert query.failureDict == {'Fail':'Fail'}


def test_download_master():
    """
    Can we iterate through a number of archives until data is found ?
    """
    master_type = 'external'
    masterDict = query.download_master(master_type)


def test_query_Master_Archive():
    
    """
    Can we query the archives of interest & download the master-list(s)?
    """
    
    # Archive's set up, so should pass
    master_type , archive = 'external', 'Zenodo'
    masterDict = query.query_Master_Archive()
    assert 'leap-seconds' in masterDict

    # Archive's not yet set up, so should fail
    master_type , archive = 'external', 'Google'
    assert query.query_Master_Archive(master_type , archive) == query.failureDict

    master_type , archive = 'external', 'MPC'
    assert query.query_Master_Archive(master_type , archive) == query.failureDict
    
    master_type , archive = 'internal', 'Zenodo'
    assert query.query_Master_Archive(master_type , archive) == query.failureDict
    
    master_type , archive = 'internal', 'Google'
    assert query.query_Master_Archive(master_type , archive) == query.failureDict
    
    master_type , archive = 'internal', 'MPC'
    assert query.query_Master_Archive(master_type , archive) == query.failureDict
    
    
    # Archive doesn't exist so should fail
    master_type , archive = 'internal', 'ArbitraryCharacterString'
    assert query.query_Master_Archive(master_type , archive) == query.failureDict





def test_read_json_from_url():
    """
    Can we read a specific url into a json file
    """
    url = 'https://zenodo.org/api/records/1458288'
    JSON_object = query.read_json_from_url(url)
    assert 'files' in JSON_object


    https://drive.google.com/open?id=1XZ-M-b5XE_MkHlGiwlDL-7J7e9mKtQzh

def test_data_item_download():
    """
    Can we download a specific item from its URL ?
    """
    itemURL      = "https://www.ietf.org/timezones/data/leap-seconds.list"
    itemFILEPATH = "leap-seconds.list"
    r = data_item_download(itemURL, itemFILEPATH)
    assert os.path.exists(itemFILEPATH)
    with open(itemFILEPATH,'r') as fh:
        data = fh.readlines()
    IN = False
    for item in data: if '2272060800' in item: IN = True
    assert IN
    print(data)


