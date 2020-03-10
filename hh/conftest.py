import pytest
from hh.app.hh import ApiHh


@pytest.fixture()
def hh():
    hh = ApiHh()
    return hh
