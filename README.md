# SpatiaLite test on Python

This example loads SpatiaLite extension and intializes spatially enabled SQLite database at the given location.

Uses SQLite that comes with python 3. Loads SpatiaLite dll as typical SQLite 3 extension.

Project contains all mod_spatialite dlls that come with mod_spatialite-4.3.0a-win-amd64 package from http://www.gaia-gis.it/gaia-sins/windows-bin-amd64/

With other OS, Python and SpatiaLite version combinations, take care to load the correct bit versions.

Tested with versions:
    
* OS: x64 Windows7

* Python: 64 bit 3.5.1, 64 bit 3.6.1

* SpatiaLite: mod_spatialite-4.3.0a-win-amd64

## Usage


Edit the last line in the PySpatialiteTest.py and replace with your setup.
createGeoDB('./TestOut/pysqlitetest4.db', './SpatialiteBin/')
