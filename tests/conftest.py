import pytest

from src.classes import Product
from src.subclasses import LawnGrass, Smartphone


@pytest.fixture
def product_1():
    return Product("LG", "4К OLED-экран", 70000.0, 3)


@pytest.fixture
def product_2():
    return Product("Sony", "HDR10+", 100000.0, 2)


@pytest.fixture
def product_3():
    return Product("Bosh", "10 различных программ", 20000.0, 4)


@pytest.fixture
def product_4():
    return Product("Test_Prod_1", "10 различных программ", 20000.0, 4)


@pytest.fixture
def product_5():
    return Product("Test_Prod_2", "10 различных программ", 20000.0, 4)


@pytest.fixture
def product_smartphone():
    return Smartphone("Siemens", "Тонкий корпус", 5000.0, 3, 10000, "E200", 16, "Purple")


@pytest.fixture
def product_smartphone_2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 30000.0, 2, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def product_lawn_grass():
    return LawnGrass("Газонная трава", "Экономный вариант", 100.0, 10, "Голландия", "5 дней", "Изумрудный")


@pytest.fixture
def product_lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 300.0, 20, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def json_info():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
