# mpcformat/tests/test_leapsec.py
# import pytest

# Third-party imports
import json

# Import the specific package/module/function we are testing
import mpcdata.create as create



def test_generate_test_master_dictionary():
    """
    Want to see the creation of a simple sample dictionary
    """
    sampleDict = create.generate_test_master_dictionary()
    assert 'leap-seconds' in sampleDict

def test_master_upload_to_Zenodo( json.dump(create.generate_test_master_dictionary()) ):
    """
    
    """
    assert 'leap-seconds' in sampleDict


