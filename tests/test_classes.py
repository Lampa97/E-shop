from src.classes import Category


def test_create_product(product_1):
    assert product_1.name == "LG"
    assert product_1.description == "4К OLED-экран"
    assert product_1.price == 70000.0
    assert product_1.quantity == 3


def test_create_categories(product_1, product_2, product_3):
    tv_products = Category("TV", "Premium class", [product_1, product_2])
    assert tv_products.name == "TV"
    assert tv_products.description == "Premium class"
    assert Category.product_count == 2
    assert Category.category_count == 1
    washing_machines = Category("Washing machines", "Очищает даже самые грязные пятна", [product_3])
    assert washing_machines.name == "Washing machines"
    assert washing_machines.description == "Очищает даже самые грязные пятна"
    assert Category.category_count == 2
    assert Category.product_count == 3
