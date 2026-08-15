from freezegun import freeze_time
import darts as DART
@freeze_time("1977-12-13")
def test_foo():
    dart =  DART.sample_darts(2).pop(0)
    assert dart.dateT == '19771213T'

