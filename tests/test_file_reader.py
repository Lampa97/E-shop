from src.file_reader import create_categories_from_json_file


def test_create_categories_from_json_file(json_info):
    categories = create_categories_from_json_file("tests/info.json")
    assert categories[0].name == "Смартфоны"
    assert categories[1].name == "Телевизоры"
