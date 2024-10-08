# SpatiaLite test on Python

This example loads SpatiaLite extension and intializes spatially enabled SQLite database at the given location. Then as a test, creates 100 thousand points, linestrings and polygons.

Uses SQLite that comes with python 3. Loads SpatiaLite dll as typical SQLite 3 extension.

Project contains all mod_spatialite dlls that come with mod_spatialite-4.3.0a-win-amd64 package from http://www.gaia-gis.it/gaia-sins/windows-bin-amd64/

With other OS, Python and SpatiaLite version combinations, take care to load the correct bit versions.

Tested with versions:
    
* OS: x64 Windows7

* Python: 64 bit 3.5.1, 64 bit 3.6.1

* SpatiaLite: mod_spatialite-4.3.0a-win-amd64

teste
## Usage
Launch IDLE from your Python distribution, then from it open PySpatialiteTest.py, and execute with F5.

Edit the call to createGeoDB (last line in the PySpatialiteTest.py) and replace with your setup, if neeeded; first argument is path to the database relative to the script, and the second is path to the mod_spatialite.dll directory.

First, it should create a spatially enabled 5,4 Mb sqlite database in TestOut directory.
Then, during test it should store several hundred thousand new entries, enlarging db up to 46 Mb.
