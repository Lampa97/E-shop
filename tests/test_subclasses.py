def test_smartphone_init(product_smartphone):
    assert product_smartphone.name == "Siemens"
    assert product_smartphone.description == "Тонкий корпус"
    assert product_smartphone.price == 5000.0
    assert product_smartphone.quantity == 3
    assert product_smartphone.efficiency == 10000
    assert product_smartphone.model == 'E200'
    assert product_smartphone.memory == 16
    assert product_smartphone.color == 'Purple'

def test_lawn_grass_init(product_lawn_grass):
    assert product_lawn_grass.name == "Газонная трава"
    assert product_lawn_grass.description == "Экономный вариант"
    assert product_lawn_grass.price == 100.0
    assert product_lawn_grass.quantity == 10
    assert product_lawn_grass.country == "Голландия"
    assert product_lawn_grass.germination_period == "5 дней"
    assert product_lawn_grass.color == 'Изумрудный'
