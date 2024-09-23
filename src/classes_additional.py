from src.classes import Category


class CategoryIterator:
    """Класс принимающий на вход объект класса Category и возвращает итератор
    с именами товаров из этой категории"""
    category_obj: Category

    def __init__(self, category_obj):
        self.category = category_obj

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index < len(self.category) - 1:
            self.index += 1
            return self.category.product_list[self.index].name
        else:
            raise StopIteration