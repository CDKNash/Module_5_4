class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)


    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f'{self.args[0]}'

    def __del__(self):
        print(f'{self.args[0]} снесён, но он останется в истории')

house1 = House('ЖК Изумрудный', 18)
print(House.houses_history)
house2 = House('Поселок ЦДК', 2)
print(House.houses_history)
house3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del house2
del house3
print(House.houses_history)
