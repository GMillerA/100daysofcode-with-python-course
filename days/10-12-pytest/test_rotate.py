import pytest

def test_rotate(string, n):
    """Test the rotate function"""
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'
    

