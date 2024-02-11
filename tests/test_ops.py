import pytest
@pytest.fixture(scope='session')
def test_add(x,y):
    assert  add(2,3) == 5
