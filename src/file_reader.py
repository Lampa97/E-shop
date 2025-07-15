import json

from src.classes import Category, Product


def create_categories_from_json_file(path: str) -> list:
    """Читает данные о товарах из json-файла и создает список состоящий из объектов класса Category"""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    categories_list = []
    for category in data:
        products_list = []
        for product in category["products"]:
            current_product = Product(product["name"], product["description"], product["price"], product["quantity"])
            products_list.append(current_product)
        current_category = Category(category["name"], category["description"], products_list)
        categories_list.append(current_category)
    return categories_list
