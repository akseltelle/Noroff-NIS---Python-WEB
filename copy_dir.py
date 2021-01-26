import cgi
from distutils.dir_util import copy_tree

data = cgi.FieldStorage()

if data.getvalue("Pleiades_large"):
    copy_tree("from", "to/Pleiades_large")
