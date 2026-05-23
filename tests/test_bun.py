import pytest

from praktikum.bun import Bun


class TestBun:
    # Параметризуем разными названиями булок, чтобы убедиться, что get_name
    # возвращает именно то название, которое было передано при создании
    @pytest.mark.parametrize("name", [
        "black bun",
        "white bun",
        "red bun",
        "sesame bun",
    ])
    def test_get_name_returns_correct_name(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name

    # Параметризуем ценами, включая граничные значения (0, дробные, большие числа)
    @pytest.mark.parametrize("price", [0, 100, 200.5, 999.99])
    def test_get_price_returns_correct_price(self, price):
        bun = Bun("test bun", price)
        assert bun.get_price() == price
