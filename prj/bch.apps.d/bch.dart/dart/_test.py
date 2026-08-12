from stamp import Stamp
from dart import dart4lines
def test_foo():
    dateT = Stamp().dateT
    dart = dart4lines([])
    assert not dart.raw.endswith('\n')
    print( 333, dateT )
    assert dart.dateT == dateT

