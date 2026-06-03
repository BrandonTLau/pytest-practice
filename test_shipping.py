import pytest
from shipping import shipping_cost

#shipping weight == 0 
def test_weight_on_boundary():
    with pytest.raises(ValueError):
        shipping_cost(0, "domestic")

#shipping weight == -1
def test_weight_below_boundary():
    with pytest.raises(ValueError):
        shipping_cost(-1, "domestic")

#incorrect destination
def test_wrong_destination():
    with pytest.raises(ValueError):
        shipping_cost(1, "USA")

#incorrect weight data type
def test_wrong_weight_data_type():
    with pytest.raises(TypeError):
        shipping_cost("heavy", "domestic")

#incorrect destination data type
def test_wrong_weight_data_type():
    with pytest.raises(Exception):
        shipping_cost(1,1)

#shipping weight == 1
def test_weight_above_boundary():
    domestic_cost = shipping_cost(1, "domestic")
    assert domestic_cost == 7

#testing domestic cost
def test_domestic_shipping_cost():
    domestic_cost = shipping_cost(2, "domestic")
    assert domestic_cost == 9

#testing international cost
def test_international_shipping_cost():
    international_cost = shipping_cost(1, "international")
    assert international_cost == 25