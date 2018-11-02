# mpcdata/mpcdata/params_masterlists.py
"""
Dictionary containing hard-coded urls at which the master-lists can be found
Once the master-lists are accessed, other files can be downloaded
The first part of the tuple is the main url stem, the later is an end/ID 
   ---   (gets used differently depending on application)
   
urlIDDict kept in a separate file "params_masterlists.py" 
   ---   This is to accommodate regular updates of the contents
"""
urlIDDict = {
    'external' :{
        'Zenodo': ('https://zenodo.org/api/records/',           '1458288' ) ,
        'Google': ('https://docs.google.com/uc?export=download','1XZ-M-b5XE_MkHlGiwlDL-7J7e9mKtQzh' ) ,
        'MPC':'',
    },
    #'internal' : {
    #    'Zenodo': '',
    #    'Google':'',
    #    'MPC':'',
    #}
}

