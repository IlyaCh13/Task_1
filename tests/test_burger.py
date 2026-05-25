import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_add_ingredient(burger, mock_sauce):
    burger.add_ingredient(mock_sauce)
    assert mock_sauce in burger.ingredients


def test_remove_ingredient(burger, mock_sauce, mock_filling):
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_filling


def test_move_ingredient(burger, mock_sauce, mock_filling):
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == mock_filling
    assert burger.ingredients[1] == mock_sauce


@pytest.mark.parametrize('bun_price, ingredient_prices, expected', [
    (100.0, [], 200.0),
    (100.0, [100.0], 300.0),
    (200.0, [100.0, 300.0], 800.0),
])
def test_get_price(burger, bun_price, ingredient_prices, expected):
    mock_bun = MagicMock()
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)
    for price in ingredient_prices:
        mock_ingredient = MagicMock()
        mock_ingredient.get_price.return_value = price
        burger.add_ingredient(mock_ingredient)
    assert burger.get_price() == expected


def test_get_receipt(burger, mock_bun, mock_sauce):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    expected = (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "(==== black bun ====)\n"
        "\n"
        "Price: 300.0"
    )
    assert burger.get_receipt() == expected


def test_get_receipt_with_filling(burger, mock_bun, mock_filling):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_filling)
    expected = (
        "(==== black bun ====)\n"
        "= filling cutlet =\n"
        "(==== black bun ====)\n"
        "\n"
        "Price: 400.0"
    )
    assert burger.get_receipt() == expected


def test_get_receipt_no_ingredients(burger, mock_bun):
    burger.set_buns(mock_bun)
    expected = (
        "(==== black bun ====)\n"
        "(==== black bun ====)\n"
        "\n"
        "Price: 200.0"
    )
    assert burger.get_receipt() == expected
