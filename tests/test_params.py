# mpcdata/tests/test_query.py
# import pytest

# Third-party imports
import os

# Import the specific package/module/function we are testing
import mpcdata.params as params
# from .context import mpcdata

def test_required_dictionaries_exist():
    """
    Does params.py contain all of the required dictionaries ?
    """
    assert hasattr(params, 'urlIDDict') # This is also testing that it's been pulled in from params_masterlists
    assert hasattr(params, 'dirDict')
    assert hasattr(params, 'fileDict')
    assert hasattr(params, 'downloadSpecDict')


def test_required_directory_paths_exist():
    """
    Does dirDict contain the required directory paths ?
    """
    for item in ['top','code','share','external','internal','test']:
        assert item in params.dirDict


def test_expected_directory_paths():
    """
    Does dirDict contain the expected directory paths ?
    """
    testDir     = os.path.realpath(os.path.dirname( __file__ ))
    topDir      = os.path.realpath(os.path.dirname( testDir ))
    shareDir    = os.path.join(topDir, 'share')
    externalDir = os.path.join(topDir, 'share','data_external')
    internalDir = os.path.join(topDir, 'share','data_internal')
    testDir     = os.path.join(topDir, 'share','data_test')
    devDir      = os.path.join(topDir, 'share','data_dev')
    
    assert topDir       == params.dirDict['top']
    assert shareDir     == params.dirDict['share']
    assert externalDir  == params.dirDict['external']
    assert internalDir  == params.dirDict['internal']
    assert testDir      == params.dirDict['test']
    assert devDir       == params.dirDict['dev']


def test_required_filepaths_are_defined():
    """
    Does fileDict contain the required directory paths ?
    """
    for item in ['external','internal']:#,'test','dev']:
        assert item in params.fileDict



def test_required_specs_exist_for_data_downloads():
    """
    Does downloadSpecDict contain the required paths ?
    """
    for item in ['attemptsMax']:
        assert item in params.downloadSpecDict
