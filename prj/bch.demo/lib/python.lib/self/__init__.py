import os
MAGIC=os.environ['SELF']
SELF = {}
for oldname, value in os.environ.items():
    if not oldname.startswith(MAGIC):
        continue
    parts = oldname.split('_')
    del parts[1]
    newname = '_'.join(parts)
    SELF[newname]=value
