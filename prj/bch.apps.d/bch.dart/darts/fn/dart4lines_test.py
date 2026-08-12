from stamp import Stamp
from darts import dart4lines
def test_foo():
    dateT = Stamp().dateT
    dart = dart4lines([])
    assert not dart.raw.endswith('\n')
    assert dart.dateT == dateT

