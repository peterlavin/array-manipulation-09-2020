
import pytest
from random import randint as ri

@pytest.fixture
def big_array():
    return [ri(1,99999) for _ in range(1,1501)]
