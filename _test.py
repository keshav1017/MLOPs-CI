import pytest


# function to test square
def square(n: int) -> int:
    return n ** 2


# function to test cube
def cube(n: int) -> int:
    return n ** 3


# function to test fifth power
def fifth(n: int) -> int:
    return n ** 5


# testing the square function
def test_square():
    assert square(2) == 4, "Test failed: Square of 2 should be 4"
    assert square(3) == 9, "Test failed: Square of 3 should be 9"


# testing the cube function
def test_cube():
    assert cube(2) == 8, "Test failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test failed: Cube of 3 should be 27"


# testing the fifth power function
def test_fifth():
    assert fifth(2) == 32, "Test failed: Fifth power of 2 should be 32"
    assert fifth(3) == 243, "Test failed: Fifth power of 3 should be 243"


# test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")

