from lib.utils.formatters import *

def test_TakeFirst():
    assert TakeFirst(['    9    ']) == '9'
    assert TakeFirst([]) is None
    assert TakeFirst([9]) is None
    assert TakeFirst(9) is None
    assert TakeFirst(None) is None