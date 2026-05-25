import pytest
import sys
import os
from unittest.mock import MagicMock

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce():
    sauce = MagicMock()
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 100.0
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce


@pytest.fixture
def mock_filling():
    filling = MagicMock()
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 200.0
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return filling
