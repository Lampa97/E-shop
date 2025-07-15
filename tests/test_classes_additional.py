import pytest

from src.classes import Category
from src.classes_additional import CategoryIterator


def test_category_iterator(product_1, product_2, product_3):
    product_set = Category("Test", "Test description", [product_1, product_2, product_3])
    iterator = iter(CategoryIterator(product_set))
    assert next(iterator) == "LG"
    assert next(iterator) == "Sony"
    assert next(iterator) == "Bosh"
    with pytest.raises(StopIteration):
        assert next(iterator)
