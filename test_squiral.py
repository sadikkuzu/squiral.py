import pytest
import squiral
from testdata_squiral import data_to_where, data_next_point

@pytest.mark.parametrize("A, direction", data_to_where)
def test_yn(A, direction):
    assert squiral.to_where(A) == direction

@pytest.mark.parametrize("row1, col1, direction, row2, col2", data_next_point)
def test_ist(row1, col1, direction, row2, col2):
    assert squiral.next_point(row1,col1,direction) == (row2,col2)
