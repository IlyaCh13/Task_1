import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize('name', ['black bun', 'white bun', 'red bun'])
def test_bun_get_name(name):
    bun = Bun(name, 100)
    assert bun.get_name() == name


@pytest.mark.parametrize('price', [0, 100, 200.5])
def test_bun_get_price(price):
    bun = Bun('test bun', price)
    assert bun.get_price() == price
