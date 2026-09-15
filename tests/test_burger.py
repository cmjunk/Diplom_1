import pytest
from unittest.mock import Mock

class TestSetBuns:
    def test_set_buns_stores_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun is mock_bun

    def test_set_buns_replaces_previous_bun(self, burger, mock_bun):
        old_bun = mock_bun

        new_bun = Mock()
        new_bun.get_name.return_value = 'another bun'
        new_bun.get_price.return_value = 300.0

        burger.set_buns(old_bun)
        burger.set_buns(new_bun)

        assert burger.bun is new_bun
        assert burger.bun is not old_bun


class TestAddIngredient:
    def test_add_ingredient_to_empty_burger(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    def test_add_multiple_ingredients_maintains_order(self, burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_3 = Mock()

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)

        assert burger.ingredients == [ingredient_1, ingredient_2, ingredient_3]


class TestRemoveIngredient:
    @pytest.mark.parametrize('index_to_remove, expected_names', [
        (0, ['b', 'c']),
        (1, ['a', 'c']),
        (2, ['a', 'b']),
    ])
    def test_remove_ingredient_by_index(self, burger, index_to_remove, expected_names):
        ingredient_a = Mock()
        ingredient_a.get_name.return_value = 'a'
        ingredient_b = Mock()
        ingredient_b.get_name.return_value = 'b'
        ingredient_c = Mock()
        ingredient_c.get_name.return_value = 'c'

        for ingredient in (ingredient_a, ingredient_b, ingredient_c):
            burger.add_ingredient(ingredient)

        burger.remove_ingredient(index_to_remove)

        remaining_names = [ing.get_name() for ing in burger.ingredients]
        assert remaining_names == expected_names

    def test_remove_ingredient_invalid_index_raises(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(IndexError):
            burger.remove_ingredient(5)


class TestMoveIngredient:
    @pytest.mark.parametrize('from_index, to_index, expected_order', [
        (0, 2, ['b', 'c', 'a']),
        (2, 0, ['c', 'a', 'b']),
        (1, 1, ['a', 'b', 'c']),
    ])
    def test_move_ingredient_reorders_list(self, burger, from_index, to_index, expected_order):
        ingredient_a = Mock()
        ingredient_a.get_name.return_value = 'a'
        ingredient_b = Mock()
        ingredient_b.get_name.return_value = 'b'
        ingredient_c = Mock()
        ingredient_c.get_name.return_value = 'c'
 
        for ingredient in (ingredient_a, ingredient_b, ingredient_c):
            burger.add_ingredient(ingredient)
 
        burger.move_ingredient(from_index, to_index)
 
        result_order = [ing.get_name() for ing in burger.ingredients]
        assert result_order == expected_order

class TestGetPrice:
    def test_get_price_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.get_price() == 200.0

    def test_get_price_with_one_ingredient(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 220.0

    @pytest.mark.parametrize('prices, expected_total', [
        ([10.0], 210.0),
        ([10.0, 20.0], 230.0),
        ([10.0, 20.0, 30.0],  260.0),
    ])
    def test_get_price_with_several_ingredients(self, burger, mock_bun, prices, expected_total):
        burger.set_buns(mock_bun)

        for price in prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_total

    def test_get_price_without_bun_raises(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()    

class TestGetReceipt:
    def test_get_receipt_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()

        expected = (
            '(==== fake bun ====)\n'
            '(==== fake bun ====)\n'
            '\n'
            'Price: 200.0'
        )
        assert receipt == expected

    def test_get_receipt_with_ingredient(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        expected = (
            '(==== fake bun ====)\n'
            '= sauce hot sauce =\n'
            '(==== fake bun ====)\n'
            '\n' 
            'Price: 220.0'
        )
        assert receipt == expected 

