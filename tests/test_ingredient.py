import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    # Параметризуем по всем возможным типам ингредиентов
    @pytest.mark.parametrize("ingredient_type", [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ])
    def test_get_type_returns_correct_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "test ingredient", 100)
        assert ingredient.get_type() == ingredient_type

    # Параметризуем разными именами ингредиентов
    @pytest.mark.parametrize("name", [
        "hot sauce",
        "sour cream",
        "cutlet",
        "dinosaur",
    ])
    def test_get_name_returns_correct_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, 150)
        assert ingredient.get_name() == name

    # Параметризуем ценами, включая граничные значения
    @pytest.mark.parametrize("price", [0, 100, 300, 999.99])
    def test_get_price_returns_correct_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", price)
        assert ingredient.get_price() == price
