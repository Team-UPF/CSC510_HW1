import pytest
from myfile import add_numbers, subtract_numbers

def test_add_numbers():
    # This test should pass
    assert add_numbers(5, 5) == 10

def test_subtract_numbers():
    # This test is intentionally made to fail
    assert subtract_numbers(10, 5) == 0
