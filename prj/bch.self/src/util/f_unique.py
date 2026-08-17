
class UniqueExc(Exception):
    """export"""
    pass

def unique( olist ):
    """
    export"""
    olist = [ x for x in olist ]
    if not len(olist) == 1:
        raise UniqueExc
    return olist[0]
