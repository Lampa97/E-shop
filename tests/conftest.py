import pytest

from src.classes import Product


@pytest.fixture
def product_1():
    return Product("LG", "4К OLED-экран", 70000.0, 3)


@pytest.fixture
def product_2():
    return Product("Sony", "HDR10+", 100000.0, 2)


@pytest.fixture
def product_3():
    return Product("Bosh", "10 различных программ", 20000.0, 4)
