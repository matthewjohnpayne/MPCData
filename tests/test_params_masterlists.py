# mpcdata/tests/test_params_masterlists.py
# import pytest

# Third-party imports
import os

# Import the specific package/module/function we are testing
import mpcdata.params_masterlists as params_masterlists



def test_required_dictionaries_exist():
    """
    Does params_masterlists.py contain all of the required dictionaries ?
    """
    assert hasattr(params, 'urlIDDict')



def test_required_urls_exist_for_master_lists():
    """
    Does urlDict contain the required paths ?
    """
    for subDict in params.urlIDDict:
        for item in ['Zenodo','Google','MPC']:
            assert item in subDict
            # assert subDict[item] # <<-- Want to add in a check on CONTENT of VALUES

