# Third-party imports
import os
#from functools import lru_cache

# Local imports
from . import params
from . import query

"""
    Master file object:
    - Provides dictionary of online locations from which specific data can be downloaded
    
    If master-file does *NOT* exist, attempts to dowload
    Once master-file exists, provides look-up dictionary, "masterDict"
    
    #  Not super-necessary to have it as an object, is barely used ...
    
    """
class MPCMasterFile(object):
    
    """
        Instantiates & populates an instance of an MPCMasterFile object
        - masterDict is the content of most-interest
        
        Parameters
        ----------
        master_type : ...
        
        Returns
        -------
        self.filepath : ...
        self.masterDict : ...
        
        Examples
        --------
        >>> ...
        
        """
    def __init__(self, master_type):#, **kwds):
        # Initiating does *EVERYTHING*, including calling "get_masterDict()"
        if master_type in fileDict:
            self.master_type =  master_type
        else:
            sys.exit("Supplied master_type, %s, is not in fileDict" % master_type )
        self.filepath    = params.fileDict[self.master_type]
        self.masterDict  = self.get_masterDict(self.filepath, self.master_type)
    
    def __str__(self):
        return 'MPCFileObject class : %s' % self.filename
    
    
    """
        Download and/or open a file containing the master-list of data sources
        
        Parameters
        ----------
        filename : ...
        master_type : ...
        
        Returns
        -------
        masterDict : ...
        
        Examples
        --------
        >>> ...
        
        """
    #@lru_cache(maxsize=params.maxcache)
    def get_masterDict(self):
        
        # If master-list file does not exist locally, download
        if not os.path.isfile(self.filepath):
            
            # Download master-list
            masterDict = query.download_master(self.master_type)
            
            # Save locally
            if len(masterDict) > 0:
                pickle.dump( masterDict, open( filepath, "wb" ) )
        
        # Open local file
        return pickle.load( open( self.filepath, "rb" ) )





"""
Generalized file object for MPC data
If file does *NOT* exist, attempts to dowload
Once file exists, allows data extraction

"""
class MPCFile(MPCMasterFile):
    
    """
    Instantiates & populates an instance of an MPCFile object
    - masterDict is the content of most-interest
    
    Parameters
    ----------
    filename : ...
     : ...
    
    Returns
    -------
    self.master_type : ...
    self.filepath : ...
    self.masterDict : ...
    
    Examples
    --------
    >>> ...
    
    """
    def __init__(self, filename):#, **kwds):
        
        self.filename                     = filename
        self.master_type, self.masterDict = self.set_master(self.filename)
        self.filepath                     = os.path.join(params.dirDict[self.master_type], self.filename)
        # self.filedata                     = self.get_filedata() ## <<-- Not doing at initialisation: just as optional call
    
    def __str__(self):
        return 'MPCFileObject class : %s' % self.filename

    #@lru_cache(maxsize=params.maxcache)
    def set_master(filename):
        # Default values
        master_type = str(None)
        masterDict  = {}
        
        # Get all possible master-types
        for loop_master_type in params.urlIDDict:
            
            # Get associated masterDict for given loop_master_type
            masterDict = MPCMasterFile(loop_master_type).get_masterDict()
            
            # If filename in masterDict, then that sets the master_type
            if filename in masterDict :
                master_type = loop_master_type
                masterDict  = masterDict

        # If no master-type set, then requested file is presumably unknown ...
        # ... (or needs to be added to one of the Master files)
        if master_type == str(None) or masterDict == {}:
            sys.exit("Supplied filename, %s, could not be found in any master-list" % self.filename)
        else:
            return master_type, masterDict


    #@lru_cache(maxsize=params.maxcache)
    def get_filedata():

        # If file does not exist locally, download
        if not os.path.isfile(self.filepath):
            
            # download file and save locally
            itemURL    = self.masterDict[self.filename]
            try:
                query.data_item_download(itemURL, self.filepath)
            except:
                sys.exit("Failed to download the URL, %s, for file %s" % (itemURL, self.filename) )
    
        # Return filepath and contents
        with open(self.filepath,'r') as f:
            self.filedata = f.readlines()
        return self.filedata

    # To be fancy and allow "with ... as ..." usage, would need to define __enter__ & __exit__
    # https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
    # https://stackoverflow.com/questions/16085292/subclassing-file-objects-to-extend-open-and-close-operations-in-python-3








if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    #return True




