import pytest
from calculator import add, subtract, multiply, divide

def test_add(): 
    result = add(0,0)
    assert result == 0

    result = add(1,1)
    assert result == 2

    result = add(-1, -2)
    assert result == -3

    result = add(1, -2)
    assert result == -1

    result = add(-1, 2)
    assert result == 1

    result = add(1.5, 1.5)
    assert result == 3

    with pytest.raises(TypeError):
        add("hello", 5)

    with pytest.raises(TypeError):
        add(5, "hello")



def test_subtract():
    result = subtract(0,0)
    assert result == 0

    result = subtract(2,1)
    assert result == 1

    result = subtract(1,2)
    assert result == -1

    result = subtract(-1, 2)
    assert result == -3

    result = subtract(1, -2)
    assert result == 3

    result = subtract(-1, -2)
    assert result == 1

    result = subtract(1.5, 1)
    assert result == 0.5

    with pytest.raises(TypeError):
        subtract("hello", 5)

    with pytest.raises(TypeError):
        subtract(5, "hello")

def test_multiply():
    result = multiply(1,0)
    assert result == 0

    result = multiply(1,1)
    assert result == 1

    result = multiply(-2, 2)
    assert result == -4

    result = multiply(-2, -2)
    assert result == 4

    result = multiply(0.5, 0.5)
    assert result == 0.25

    with pytest.raises(TypeError):
        multiply("hello", 5)

    with pytest.raises(TypeError):
        multiply(5, "hello")



def test_divide():

    
    result = divide(1,1)
    assert result == 1

    result = divide(-2, 2)
    assert result == -1

    result = divide(-2, -2)
    assert result == 1

    result = divide(0.5, 0.5)
    assert result == 1

    # BVA - boundary around b=0
    result = divide(10, 1)   # just above boundary - valid
    assert result == 10

    result = divide(10, -1)  # just below boundary - valid
    assert result == -10

    with pytest.raises(TypeError):
        divide("hello", 5)

    with pytest.raises(TypeError):
        divide(5, "hello")

    with pytest.raises(ValueError):
        divide(10, 0)
    