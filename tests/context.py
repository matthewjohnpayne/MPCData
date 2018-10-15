# Use a simple (but explicit) path modification to resolve the package properly.
import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mpcdata  

