# mpcdata/mpcdata/query.py

# Third-party imports
import sys
import json
import urllib.request
import requests

# Import local modules
import mpcdata.params as params


"""
Allow easy management/detection of failure
"""
failureDict = {'Fail':'Fail'}




def download_master(master_type):
    """
    Make repeated attempts to download a "master list" (in JSON format) from a variety of sources.
    Manage failure
    
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
    # Allow easy management/detection of download-failure
    masterDict = failureDict.copy()
    
    # Get the urls that need to be looked at
    thisURLDict = params.urlIDDict[master_type]
    
    # We are going to try downloading the data from Zenodo/Google/MPC
    for archive in params.archiveNameList: # I.e. looping over Zenodo/Google/MPC
        # Attempt to download
        attempts = 0
        while masterDict == failureDict and attempts < params.downloadSpecDict['attemptsMax'] :
            masterDict = query_Master_Archive(master_type , archive)
            attempts   += 1

    # Did any of the download-attempts succeed?
    try:
        assert masterDict != failureDict
    except Exception as e:
        print(type(e))
        #print("Failed to download anything for %s: likely because archive not recognized" % archive )
        sys.exit("Failed to download anything for %s: likely because archive not recognized" % archive )
    
    return masterDict



def query_Master_Archive(master_type , archive):
    """
    Make a one-off attempt to download a "master list" (in JSON format) from one of Zenodo/Google/MPC
    
    Parameters
    ----------
    master_type : one from ['external','internal',...]
    archive : one from ['Zenodo','Google','MPC']
    
    Returns
    -------
    ...
    
    Examples
    --------
    >>> ...
    
    """

    # Default to failure ...
    masterDict  = failureDict.copy()
    
    if archive == 'Zenodo':
        try:
            # Use the master url to get the name of latest constituent file
            url = params.urlIDDict[master_type][archive][0] + params.urlIDDict[master_type][archive][1]
            JSON_object = read_json_from_url( url )
            
            # The headline json from Zenodo contains the name of ...
            # ... the latest upload-json within it
            latestURL   = JSON_object['files'][-1]['links']['self']
        
            # Download the specific JSON containing the latest master-list
            masterDict  = read_json_from_url(latestURL)
        
        except Exception as e:
            print(type(e))

    if archive == 'Google':
        try:
            # Download from google
            url, id  = params.urlIDDict[master_type][archive][0] , params.urlIDDict[master_type][archive][1]
            session  = requests.Session()
            response = session.get(url, params = { 'id' : id }, stream = True)
        
            # Convert master-list to dictionary format
            masterDict = response.json()

        except Exception as e:
            print(type(e))

    if archive == 'MPC':
        try:
            pass
        
        except Exception as e:
            print(type(e))

    try:
        assert masterDict != failureDict
    except Exception as e:
        print("Failed to download anything for %s: likely because archive not recognized" % archive )
        print(type(e))

    return masterDict



def download_master_file_from_google_drive(url, ID):
    """
    Convenience function to download a file from google drive and save it to file
    # https://github.com/nsadawi/Download-Large-File-From-Google-Drive-Using-Python/blob/master/Download-Large-File-from-Google-Drive.ipynb
    
    Parameters
    ----------
    url :
    ID :
    
    Returns
    -------
    masterDict :
    
    Examples
    --------
    >>> ...
    
    """
    session = requests.Session()
    response   = session.get(url, params = { 'id' : id }, stream = True)
    
    masterDict = response.json()
    return masterDict
    




def read_json_from_url(url):
    """
    Convenience function to read a json-formatted-URL into a JSON-object
    
    Parameters
    ----------
    url :
    
    Returns
    -------
    JSON_object
    
    Examples
    --------
    >>> ...
    
    """
    webURL    = urllib.request.urlopen(url)
    encoding  = webURL.info().get_content_charset('utf-8')
    JSON_object = json.loads(webURL.read().decode(encoding))
    return JSON_object


def data_item_download(itemURL, itemFILEPATH):
    """
    Convenience function to download an arbitrary url and save it to file
    
    Parameters
    ----------
    itemURL :
    itemFILEPATH :
    
    Returns
    -------
    ...
    
    Examples
    --------
    >>> ...
    
    """
    return urllib.request.urlretrieve(itemURL, itemFILEPATH )


