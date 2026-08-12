# This was intended to be an __init__.py file
from import_tool import dopath
from pathlib import Path
here = str(Path(__file__).parent)
for line in dopath(here):
    print(line)
    exec(line)
