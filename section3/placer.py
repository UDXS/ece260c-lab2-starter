

# Importing the OpenROAD library - which is only available when running openroad -python
from openroad import Design, Tech
from odb import *
from pathlib import Path


# If we had a separate .lef, we could run tech.readLef but we're using a db here that comes packaged with the library.
tech = Tech()
# We do still need to load the Liberty because OpenDB doesn't store enough information for OpenSTA to run correctly.
tech.readLiberty("../sg13g2_stdcell_typ_1p20V_25C.lib")

design = Design(tech) # Every Design has to be associated with a Tech, even if it's empty.

design.readDb("section3.odb")
library = design.getDb().getLibs()[0] # This gets the only loaded library - the IHP130 PDK
dbu_per_micron = library.getDbUnitsPerMicron()
cam_vertical_offset = library.getSites()[0].getHeight()
block = design.getBlock()

origin_x = 120000
origin_y = 60000
def decode_cam_index(name):
    return int(name.removeprefix("cam\\[").split("\\")[0])

# TODO: When you're writing scripts, write your code below this line:



# Write the DB back out to a file.
# If you make no changes, then the DBs should be no different.
design.writeDb(f"{Path(__file__).stem}.odb")

# By default, OpenROAD will drop into an interactive Python REPL after your script finishes.
# This makes it possible to explore the Python API using Tab completion or the dir() function.
# You can use the exit command to drop out of this REPL once you're done with it. 
# If you do not want it to appear at all, then use openroad -python -exit my_script.py