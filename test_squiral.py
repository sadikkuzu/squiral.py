import pytest

import squiral
from testdata_squiral import data_next_point
from testdata_squiral import data_to_where


@pytest.mark.parametrize("A, direction", data_to_where)
def test_to_where(A, direction):
    assert squiral.to_where(A) == direction


@pytest.mark.parametrize("row1, col1, direction, row2, col2", data_next_point)
def test_next_point(row1, col1, direction, row2, col2):
    assert squiral.next_point(row1, col1, direction) == (row2, col2)


def test_directions():
    assert squiral.directions is not None


def test_produce0():
    assert squiral.produce(0) is None


def test_produce1():
    assert squiral.produce(1) == [[1]]


def test_produce2():
    assert squiral.produce(2) == [[1, 2], [4, 3]]
