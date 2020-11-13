import pytest
import os

from vxml.error import VXML_Error

def test_error_get_kind():
	err = VXML_Error(kind = 'Leak_StillReachable')	
	assert err.get_kind() == 'Leak_StillReachable'

