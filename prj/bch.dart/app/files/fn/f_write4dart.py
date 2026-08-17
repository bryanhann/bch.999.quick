from constants import ACC
dst=ACC/'acc.darts'
def write4dart(dart):
    print( f"{ACC=}" )
    with dst.open( 'a' )  as fd:
        fd.write( f"{dart}\n" )
    print( dst.read_text() ) 
