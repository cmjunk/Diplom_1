import pytest

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    return Database()


class TestAvailableBuns:
    def test_returns_list(self, database):
        buns = database.available_buns()

        assert isinstance(buns, list)

    def test_returns_correct_amount(self, database):
        buns = database.available_buns()

        assert len(buns) == 3

    def test_all_items_are_bun_instances(self, database):
        buns = database.available_buns()

        assert all(isinstance(bun, Bun) for bun in buns)

    @pytest.mark.parametrize('index, expected_name, expected_price', [
        (0, 'black bun', 100),
        (1, 'white bun', 200),
        (2, 'red bun', 300),
    ])
    def test_bun_contents(self, database, index, expected_name, expected_price):
        buns = database.available_buns()

        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    def test_returns_same_list_reference(self, database):
        buns_first_call = database.available_buns()
        buns_second_call = database.available_buns()

        assert buns_first_call is buns_second_call


class TestAvailableIngredients:
    def test_returns_list(self, database):
        ingredients = database.available_ingredients()

        assert isinstance(ingredients, list)

    def test_returns_correct_amount(self, database):
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

    def test_all_items_are_ingredient_instances(self, database):
        ingredients = database.available_ingredients()

        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    @pytest.mark.parametrize('index, expected_type, expected_name, expected_price', [
        (0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
        (2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
        (3, INGREDIENT_TYPE_FILLING, 'cutlet', 100),
        (4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
        (5, INGREDIENT_TYPE_FILLING, 'sausage', 300),
    ])
    def test_ingredient_contents(self, database, index, expected_type, expected_name, expected_price):
        ingredients = database.available_ingredients()

        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price

    def test_returns_same_list_reference(self, database):
        ingredients_first_call = database.available_ingredients()
        ingredients_second_call = database.available_ingredients()

        assert ingredients_first_call is ingredients_second_call