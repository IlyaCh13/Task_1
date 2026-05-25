import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
def test_ingredient_get_type(ingredient_type):
    ingredient = Ingredient(ingredient_type, 'test', 100)
    assert ingredient.get_type() == ingredient_type


@pytest.mark.parametrize('name', ['hot sauce', 'cutlet', 'sour cream'])
def test_ingredient_get_name(name):
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
    assert ingredient.get_name() == name


@pytest.mark.parametrize('price', [0, 100, 300])
def test_ingredient_get_price(price):
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'test', price)
    assert ingredient.get_price() == price
