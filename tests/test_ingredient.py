import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

INGREDIENT_CASES = [
    (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100.0),
    (INGREDIENT_TYPE_SAUCE, 'sour cream', 200.0),
    (INGREDIENT_TYPE_FILLING, 'cutlet', 100.0),
    (INGREDIENT_TYPE_FILLING, 'dinosaur', 200.0),
]

class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENT_CASES)

    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENT_CASES)
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', INGREDIENT_CASES)
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
