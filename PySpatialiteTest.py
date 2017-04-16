import sqlite3
import os

# This example loads SpatiaLite extension and intializes
# geo database at the given database.

# Load SpatiaLite extension as typical SQLite 3 extension
# Be sure to load the correct extension (x32 or x64, etc.)

# Use sqlite3 that comes with Python 3.5.
# Tested on x64 Windows7, x64 Python 3.5.1 and 3.6.1

def createGeoDB(dbname, SpatiaLitePath):
        con = sqlite3.connect(dbname)
        con.enable_load_extension(True)

        # Next line is very important. Without it, mod_spatialite library will not find
        # dlls it depends on. 
        os.environ['PATH'] = SpatiaLitePath + ';' + os.environ['PATH']
        con.load_extension(os.path.join(SpatiaLitePath, 'mod_spatialite'))
        cur = con.cursor()    
        cur.execute('SELECT InitSpatialMetaData(1)')
        con.commit()
        con.close()


# Load SpatiaLite from relative path and save database to relative path
createGeoDB('./TestOut/pysqlitetest4.db', './SpatialiteBin/')
