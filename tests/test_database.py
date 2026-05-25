from unittest.mock import patch
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_available_buns_returns_list():
    db = Database()
    assert isinstance(db.available_buns(), list)


def test_available_buns_count():
    db = Database()
    assert len(db.available_buns()) == 3


def test_available_buns_are_bun_instances():
    db = Database()
    for bun in db.available_buns():
        assert isinstance(bun, Bun)


def test_available_ingredients_returns_list():
    db = Database()
    assert isinstance(db.available_ingredients(), list)


def test_available_ingredients_count():
    db = Database()
    assert len(db.available_ingredients()) == 6


def test_available_ingredients_are_ingredient_instances():
    db = Database()
    for ingredient in db.available_ingredients():
        assert isinstance(ingredient, Ingredient)


def test_available_ingredients_include_sauces():
    db = Database()
    types = [i.get_type() for i in db.available_ingredients()]
    assert INGREDIENT_TYPE_SAUCE in types


def test_available_ingredients_include_fillings():
    db = Database()
    types = [i.get_type() for i in db.available_ingredients()]
    assert INGREDIENT_TYPE_FILLING in types


def test_database_creates_three_buns():
    with patch('praktikum.database.Bun') as mock_bun_class:
        mock_bun_class.return_value = mock_bun_class
        Database()
        assert mock_bun_class.call_count == 3


def test_database_creates_six_ingredients():
    with patch('praktikum.database.Ingredient') as mock_ingredient_class:
        mock_ingredient_class.return_value = mock_ingredient_class
        Database()
        assert mock_ingredient_class.call_count == 6
