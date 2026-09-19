import pytest

from praktikum.bun import Bun

BUN_CASES = [
    ('black bun', 100.0),
    ('white bun', 200.0),
    ('red bun', 300.0),
]


class TestBun:
    @pytest.mark.parametrize('name, price', BUN_CASES)
    def test_get_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', BUN_CASES)
    def test_get_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price

    def test_get_name_returns_str(self):
        bun = Bun('black bun', 100.0)

        assert isinstance(bun.get_name(), str)

    def test_get_price_returns_number(self):
        bun = Bun('black bun', 100.0)

        assert isinstance(bun.get_price(), (int, float))
