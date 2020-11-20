''' Unit Tests for error module '''
from vxml import VXMLError

def test_error_get_kind():
    ''' Test error get_kind function '''
    err = VXMLError(kind='Leak_StillReachable')
    assert err.get_kind() == 'Leak_StillReachable'


def test_error_print():
    ''' Test error __str__ work '''
    err = VXMLError(kind='Leak_StillReachable')
    print(err)
