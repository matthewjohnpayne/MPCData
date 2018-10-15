# mpcformat/tests/test_leapsec.py
# import pytest

# Third-party imports
import json

# Import the specific package/module/function we are testing
import mpcdata.mpcdata as mpcdata



def test_MPCMasterFile():
    """
    Want to see the successful return of a masterDict from an MPCMasterFile object
    ... both when a local master-file already exists and when it doesn't
    """
    
    for master_type in ['external', 'internal']:
    
        # Forcibly delete any local master-file ('external_master_list.txt')
        filepath = params.fileDict[master_type]
        try:
            os.remove(filepath)
        except OSError:
            pass
        assert not os.path.exists(filepath)

        # Running open_master_list should
        # (i) generate a filepath
        # (ii) download a masterDict & save-it to disk
        MPCMF = mpcdata.MPCMasterFile(master_type)
        filepath   = MPCMF.filepath
        masterDict = MPCMF.masterDict
        assert os.path.exists(filepath)
        assert 'leap-seconds' in masterDict

        # Running open_master_list again should just cause a fileread (no download)
        modtimeBefore = os.path.getmtime(filepath)
        MPCMF = mpcdata.MPCMasterFile(master_type)
        filepath   = MPCMF.filepath
        masterDict = MPCMF.masterDict
        modtimeAfter = os.path.getmtime(filepath)
        assert modtimeAfter == modtimeBefore
        assert 'leap-seconds' in masterDict


def test_MPCMasterFile_for_nonexistant_type():
    """
    Want to check what happens when a nonexistant master-list-type is passed 
    This test prob won't work due to poor exception handling
    """
    master_type = 'ThisStringShouldNotWork'
    
    try:
        MPCMF = mpcdata.MPCMasterFile(master_type)
        passed = True
    except:
        passed = False
    assert not passed


def test_MPCFile_external():
    """
    Want to see the successful return of a filepath & filecontents from MPCFile object
    ... both when the local file already exists and when it doesn't
    This is for some EXTERNAL (i.e. non-MPC) file
    """

    filename = 'leap-seconds.txt'
    master_type ='external'
    expectedfilepath = os.path.join(params.dirDict[master_type],filename)

    # Forcibly delete any local data file
    try:
        os.remove(expectedfilepath)
    except OSError:
        pass
    assert not os.path.exists(expectedfilepath)

    # Initiating an MPCFile object should allow access to filepath variable
    MPCF = mpcdata.MPCFile(filename)
    filepath = MPCF.filename
    assert filepath == expectedfilepath

    # Because of the above deletes and that we did NOT download, we expect filepath to still NOT exist
    assert not os.path.exists(filepath)

    # Calling get_filedata() method should cause the file to come into existence
    filedata = MPCF.get_filedata()
    assert os.path.exists(filepath)
    assert filedata = MPCF.filedata

    # The 'leap-seconds.txt' file is expected to contain the string '2272060800' at some point
    IN = False ; for item in filedata: if '2272060800' in item: IN = True
    assert IN

    # Running MPCF.get_filedata() again should just cause a fileread (no download)
    modtimeBefore = os.path.getmtime(expectedfilepath)
    MPCF           = mpcdata.MPCFile(filename)
    filedata       = MPCF.get_filedata()
    modtimeAfter   = os.path.getmtime(expectedfilepath)
    assert modtimeAfter == modtimeBefore
    assert 'leap-seconds' in masterDict


'''
def test_MPCFile_internal():
    """
        Want to see the successful return of a filepath & filecontents from MPCFile object
        ... both when the local file already exists and when it doesn't
        This is for some INTERNAL file (i.e. from MPC website)
        """
    
    filename = '?????.txt'
    master_type ='internal'
    expectedfilepath = os.path.join(params.dirDict[master_type],filename)
    
    # Forcibly delete any local file
    try:
        os.remove(expectedfilepath)
    except OSError:
        pass
    assert not os.path.exists(expectedfilepath)

    # Initiating an MPCFile object should allow access to filepath variable
    MPCF = mpcdata.MPCFile(filename)
    filepath = MPCF.filename
    assert filepath == expectedfilepath
    
    # Because of the above deletes and that we did NOT download, we expect filepath to still NOT exist
    assert not os.path.exists(filepath)
    
    # Calling get_filedata() method should cause the file to come into existence
    filedata = MPCF.get_filedata()
    assert os.path.exists(filepath)
    assert filedata = MPCF.filedata
    
    # The 'leap-seconds.txt' file is expected to contain the string '2272060800' at some point
    IN = False ; for item in filecontents: if '2272060800' in item: IN = True
    assert IN
    
    # Running MPCF.get_filedata() again should just cause a fileread (no download)
    modtimeBefore = os.path.getmtime(expectedfilepath)
    MPCF           = mpcdata.MPCFile(filename)
    filedata       = MPCF.get_filedata()
    modtimeAfter   = os.path.getmtime(expectedfilepath)
    assert modtimeAfter == modtimeBefore
    assert 'leap-seconds' in masterDict
'''

