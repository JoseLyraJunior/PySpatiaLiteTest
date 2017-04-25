import sqlite3
import os

# This example loads SpatiaLite extension and intializes
# geo database at the given database.

# Load SpatiaLite extension as typical SQLite 3 extension
# Be sure to load the correct extension (x32 or x64, etc.)

# Use sqlite3 that comes with Python 3.5.
# Tested on x64 Windows7, x64 Python 3.5.1 and 3.6.1

def createGeoDB(dbname, SpatiaLitePath):
    """Create and initialize a geodatabase"""
    con = sqlite3.connect(dbname)
    con.enable_load_extension(True)

    # Next line is very important. Without it, mod_spatialite library will not find
    # dlls it depends on.
    os.environ['PATH'] = SpatiaLitePath + ';' + os.environ['PATH']
    con.load_extension(os.path.join(SpatiaLitePath, 'mod_spatialite'))
    cur = con.cursor()
    cur.execute('SELECT InitSpatialMetaData(1)')

    test(con)

    con.commit()
    con.close()


def test(conn):
    """Test function taken from http://www.gaia-gis.it/spatialite-2.4.0-4/splite-python.html."""

    cur = conn.cursor()
    rs = cur.execute('SELECT sqlite_version(), spatialite_version()')

    for row in rs:
        msg = "> SQLite v%s Spatialite v%s" % (row[0], row[1])
        print(msg)

    sql = """CREATE TABLE test_pt (id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL)"""
    cur.execute(sql)

    # creating a POINT Geometry column
    sql = "SELECT AddGeometryColumn('test_pt', 'geom', 4326, 'POINT', 'XY')"
    cur.execute(sql)

    # creating a LINESTRING table
    sql = """CREATE TABLE test_ln (id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL)"""
    cur.execute(sql)

    # creating a LINESTRING Geometry column
    sql = "SELECT AddGeometryColumn('test_ln', 'geom', 4326, 'LINESTRING', 'XY')"
    cur.execute(sql)

    # creating a POLYGON table
    sql = """CREATE TABLE test_pg ( id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL)"""
    cur.execute(sql)

    # creating a POLYGON Geometry column
    sql = """SELECT AddGeometryColumn('test_pg', 'geom', 4326, 'POLYGON', 'XY')"""
    cur.execute(sql)

    # inserting some POINTs
    # please note well: SQLite is ACID and Transactional
    # so (to get best performance) the whole insert cycle
    # will be handled as a single TRANSACTION
    for i in range(100000):
        name = "test POINT #%d" % (i+1)
        geom = "GeomFromText('POINT("
        geom += "%f " % (i / 1000.0)
        geom += "%f" % (i / 1000.0)
        geom += ")', 4326)"
        sql = "INSERT INTO test_pt (id, name, geom) "
        sql += "VALUES (%d, '%s', %s)" % (i+1, name, geom)
        cur.execute(sql)

    conn.commit()

    # checking POINTs
    sql = "SELECT DISTINCT Count(*), ST_GeometryType(geom), ST_Srid(geom) FROM test_pt"
    rs = cur.execute(sql)
    for row in rs:
        msg = "> Inserted %d entities of type " % (row[0])
        msg += "%s SRID=%d" % (row[1], row[2])
        print(msg)

    # inserting some LINESTRINGs
    for i in range(100000):
        name = "test LINESTRING #%d" % (i+1)
        geom = "GeomFromText('LINESTRING("
        if (i%2) == 1:
        # odd row: five points
            geom += "-180.0 -90.0, "
            geom += "%f " % (-10.0 - (i / 1000.0))
            geom += "%f, " % (-10.0 - (i / 1000.0))
            geom += "%f " % (10.0 + (i / 1000.0))
            geom += "%f" % (10.0 + (i / 1000.0))
            geom += ", 180.0 90.0"
        else:
        # even row: two points
            geom += "%f " % (-10.0 - (i / 1000.0))
            geom += "%f, " % (-10.0 - (i / 1000.0))
            geom += "%f " % (10.0 + (i / 1000.0))
            geom += "%f" % (10.0 + (i / 1000.0))
        geom += ")', 4326)"
        sql = "INSERT INTO test_ln (id, name, geom) "
        sql += "VALUES (%d, '%s', %s)" % (i+1, name, geom)
        cur.execute(sql)

    conn.commit()

    # checking LINESTRINGs
    sql = "SELECT DISTINCT Count(*), ST_GeometryType(geom), ST_Srid(geom) FROM test_ln"
    rs = cur.execute(sql)

    for row in rs:
        msg = "> Inserted %d entities of type " % (row[0])
        msg += "%s SRID=%d" % (row[1], row[2])
        print (msg)

    # inserting some POLYGONs
    for i in range(100000):
        name = "test POLYGON #%d" % (i+1)
        geom = "GeomFromText('POLYGON(("
        geom += "%f " % (-10.0 - (i / 1000.0))
        geom += "%f, " % (-10.0 - (i / 1000.0))
        geom += "%f " % (10.0 + (i / 1000.0))
        geom += "%f, " % (-10.0 - (i / 1000.0))
        geom += "%f " % (10.0 + (i / 1000.0))
        geom += "%f, " % (10.0 + (i / 1000.0))
        geom += "%f " % (-10.0 - (i / 1000.0))
        geom += "%f, " % (10.0 + (i / 1000.0))
        geom += "%f " % (-10.0 - (i / 1000.0))
        geom += "%f" % (-10.0 - (i / 1000.0))
        geom += "))', 4326)"
        sql = "INSERT INTO test_pg (id, name, geom) VALUES (%d, '%s', %s)" % (i+1, name, geom)
        cur.execute(sql)

    conn.commit()

    # checking POLYGONs
    sql = "SELECT DISTINCT Count(*), ST_GeometryType(geom), ST_Srid(geom) FROM test_pg"
    rs = cur.execute(sql)

    for row in rs:
        msg = "> Inserted %d entities of type " % (row[0])
        msg += "%s SRID=%d" % (row[1], row[2])
        print(msg)

    rs.close()

# Load SpatiaLite from relative path and save database to relative path
createGeoDB('./TestOut/pysqlitetest4.db', './SpatialiteBin/')
