
#tests

from app.Utilities import to_usd

#def test answer():
   # assert 


def test_to_usd():
    assert to_usd(123456789.98) == "$123,456,789.98"
    assert to_usd(0.4555) == "$0.46"