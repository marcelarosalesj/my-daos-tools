import pytest
import os

from vxml import VXML_Error

def test_error_get_kind():
	err = VXML_Error(kind = 'Leak_StillReachable')	
	assert err.get_kind() == 'Leak_StillReachable'


def test_error_print():
	err = VXML_Error(kind = 'Leak_StillReachable')	
	print(err)
	
