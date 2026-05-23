from unittest.mock import patch

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns_returns_list(self):
        db = Database()
        result = db.available_buns()
        assert isinstance(result, list)

    def test_available_buns_count(self):
        db = Database()
        # В базе должно быть ровно 3 булочки
        assert len(db.available_buns()) == 3

    def test_available_buns_contain_bun_instances(self):
        db = Database()
        for bun in db.available_buns():
            assert isinstance(bun, Bun)

    def test_available_ingredients_returns_list(self):
        db = Database()
        result = db.available_ingredients()
        assert isinstance(result, list)

    def test_available_ingredients_count(self):
        db = Database()
        # В базе должно быть ровно 6 ингредиентов
        assert len(db.available_ingredients()) == 6

    def test_available_ingredients_contain_ingredient_instances(self):
        db = Database()
        for ingredient in db.available_ingredients():
            assert isinstance(ingredient, Ingredient)

    def test_available_ingredients_include_sauces(self):
        db = Database()
        types = [i.get_type() for i in db.available_ingredients()]
        assert INGREDIENT_TYPE_SAUCE in types

    def test_available_ingredients_include_fillings(self):
        db = Database()
        types = [i.get_type() for i in db.available_ingredients()]
        assert INGREDIENT_TYPE_FILLING in types

    # Мокируем конструктор Bun, чтобы убедиться, что Database его вызывает
    # и не зависит от конкретной реализации Bun
    def test_database_calls_bun_constructor(self):
        with patch("praktikum.database.Bun") as mock_bun_class:
            mock_bun_class.return_value = mock_bun_class
            Database()
            assert mock_bun_class.call_count == 3

    # Мокируем конструктор Ingredient аналогично
    def test_database_calls_ingredient_constructor(self):
        with patch("praktikum.database.Ingredient") as mock_ingredient_class:
            mock_ingredient_class.return_value = mock_ingredient_class
            Database()
            assert mock_ingredient_class.call_count == 6
