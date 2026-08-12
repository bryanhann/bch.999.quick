from freezegun import freeze_time
import dart as DART
@freeze_time("1977-12-13")
def test_foo():
    dart =  DART.darts().pop(0)
    assert dart.dateT == '19771213T'

