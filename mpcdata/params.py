import os

import params_masterlists

"""
Dictionary containing hard-coded urls at which the master-lists can be found
Once the master-lists are accessed, other files can be downloaded
The first part of the tuple is the main url stem, the later is an end/ID 
   ---   (gets used differently depending on application)
   
urlIDDict kept in a separate file "params_masterlists.py"
   ---   This is to accommodate regular updates of the contents
"""
urlIDDict = params_masterlists.urlIDDict
archiveNameList = ['Zenodo','Google','MPC']

"""
Dictionary containing filepaths for package directory structure
"""
codeDir   = os.path.realpath(os.path.dirname( __file__ ))
topDir    = os.path.realpath(os.path.dirname( codeDir ))

dirDict   = {
    'top':topDir ,
    'code':codeDir ,
    'share':    os.path.join(topDir, 'share'),
    'external': os.path.join(topDir, 'share', 'data_external'),
    'internal': os.path.join(topDir, 'share', 'data_internal'),
    'test':     os.path.join(topDir, 'share', 'data_test'),
    'dev':      os.path.join(topDir, 'share', 'data_dev'),
}

"""
Dictionary containing specific filenames
"""
fileDict = {
    'external': os.path.join(dirDict['external'] , 'external_master_list.txt'),
    'internal': os.path.join(dirDict['internal'] , 'internal_master_list.txt'),
}

"""
When attempting external downloads, how patient should we be?
"""
downloadSpecDict = {
    'attemptsMax' : 2,
    'attemptWait' : 5, # Currently unused
}

"""
When caching, how many to cache
"""
maxcache = 128
