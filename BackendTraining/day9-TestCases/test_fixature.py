import pytest

@pytest.fixture
def defaultInput():
    x = 50+50
    return x

def test_mult(defaultInput):
    assert defaultInput*10 == 1000
    
def test_divisible(defaultInput):
    assert defaultInput/10 == 10
