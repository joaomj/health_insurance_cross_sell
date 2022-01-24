# This file was adapted from http://www.postgresqltutorial.com/postgresql-python/connect/ 
# and https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43 

# The following config() function reads in the database.ini file and returns the connection
# parameters as a dictionary. This function will be imported in to the main python script/notebook:

#!/usr/bin/python
from configparser import ConfigParser

import os
import sys
from pathlib import Path
 
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()

    # defining file path
    path = str(Path.cwd().parents[0] / "src" / "data")
    filename_ = path + '/' + filename

    # check file path
    if os.path.isfile(filename_):

        # read config file
        parser.read(filename_)

        # get section, default to postgresql
        db = {}
        
        # Checks to see if section (postgresql) parser exists
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
            
        # Returns an error if a parameter is called that is not listed in the initialization file
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    
    else:
        raise Exception('File {} not found in location'.format(filename_))

    return db