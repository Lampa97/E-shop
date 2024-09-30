import pytest
from src.classes import Category, Product


def test_create_product(product_1):
    assert product_1.name == "LG"
    assert product_1.description == "4К OLED-экран"
    assert product_1.price == 70000.0
    assert product_1.quantity == 3


def test_create_categories(product_1, product_2, product_3):
    tv_products = Category("TV_Products", "Premium class", [product_1, product_2])
    assert tv_products.name == "TV_Products"
    assert tv_products.description == "Premium class"
    assert tv_products.product_count == 2
    assert Category.category_count == 1
    washing_machines = Category("Washing machines", "Очищает даже самые грязные пятна", [product_3])
    assert washing_machines.name == "Washing machines"
    assert washing_machines.description == "Очищает даже самые грязные пятна"
    assert Category.category_count == 2
    assert washing_machines.product_count == 3


def test_add_products(product_4, product_5):
    test_products = Category("Test_Prods", "Test_description", [product_4])
    test_products.add_product(product_5)
    assert test_products.product_count == 5


def test_set_price(product_1):
    product_1.price = 100000
    assert product_1.price == 100000


def test_set_price_negative(capsys, product_1):
    product_1.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_new_product(product_1):
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_make_string_products(product_1, product_2):
    tv_products = Category("TV", "Premium class", [product_1, product_2])
    assert (
        tv_products.products
        == f"""{product_1.name}, {product_1.price} руб. Остаток: {product_1.quantity} шт.
{product_2.name}, {product_2.price} руб. Остаток: {product_2.quantity} шт.\n"""
    )


def test_add_method_products(product_1, product_2):
    assert product_1 + product_2 == 410000.0


def test_str_product(product_1):
    assert str(product_1) == "LG, 70000.0 руб. Остаток: 3 шт."


def test_str_category(product_1, product_2):
    tv_products = Category("TV", "Premium class", [product_1, product_2])
    assert str(tv_products) == "TV, количество продуктов: 5 шт."

def test_add_same_product(product_smartphone, product_smartphone_2, product_lawn_grass, product_lawn_grass_2):
    assert product_smartphone + product_smartphone_2 == 75000.0
    assert product_lawn_grass + product_lawn_grass_2 == 7000.0

def test_add_different_products(product_smartphone_2, product_lawn_grass_2):
    with pytest.raises(TypeError):
        assert product_smartphone_2 + product_lawn_grass_2

def test_add_not_product():
    with pytest.raises(TypeError):
        assert Category.add_product('Wrong Product')
