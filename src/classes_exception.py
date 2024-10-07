class ZeroQuantityProduct(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Нельзя добавлять товар с нулевым или отрицательным количеством'

    def __str__(self):
        return self.message