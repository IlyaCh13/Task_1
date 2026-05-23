import pytest
from unittest.mock import MagicMock

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    # Фикстура создаёт бургер перед каждым тестом, чтобы тесты были независимы
    @pytest.fixture
    def burger(self):
        return Burger()

    # Мок булки — нас интересует только поведение Burger,
    # поэтому зависимость Bun заменяем моком
    @pytest.fixture
    def mock_bun(self):
        bun = MagicMock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100.0
        return bun

    @pytest.fixture
    def mock_sauce(self):
        sauce = MagicMock()
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 100.0
        sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        return sauce

    @pytest.fixture
    def mock_filling(self):
        filling = MagicMock()
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 200.0
        filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        return filling

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients

    def test_add_multiple_ingredients(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert len(burger.ingredients) == 2

    def test_remove_ingredient(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        # После удаления первого элемента должен остаться только mock_filling
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_filling

    def test_move_ingredient(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # Перемещаем первый ингредиент на позицию 1
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    # Параметризуем разными ценами булки и ингредиентов,
    # чтобы убедиться, что формула (bun*2 + ingredients) работает корректно
    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", [
        (100.0, [], 200.0),
        (100.0, [100.0], 300.0),
        (200.0, [100.0, 300.0], 800.0),
        (0.0, [0.0], 0.0),
    ])
    def test_get_price(self, burger, bun_price, ingredient_prices, expected_total):
        mock_bun = MagicMock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = MagicMock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_total

    def test_get_receipt_contains_bun_name(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        assert "black bun" in receipt

    def test_get_receipt_contains_ingredient_name(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        assert "hot sauce" in receipt

    def test_get_receipt_contains_price(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        # bun(100)*2 + sauce(100) = 300
        receipt = burger.get_receipt()
        assert "300" in receipt

    def test_get_receipt_bun_appears_twice(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        # Булочка должна быть сверху и снизу бургера
        assert receipt.count("black bun") == 2
