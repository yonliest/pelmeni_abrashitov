class Product:
    def __init__(self, name:str, cost:float, weight:float, count:int, quality:float):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.count = count
        self.quality = quality
    def __str__(self):
        return self.name + " стоят: " + str(self.cost) + " рублей за: " + str(self.weight) + " кг, в упаковке: " + str(self.count) + " пельменей. Качество товара: " + str(self.quality) + " из 5"


class CommandInput:
    def __init__(self, command_str: str):
        command_split = command_str.split(" ")

        self.command = command_split[0]
        self.params = command_split[1:]

class Prorab:
    def __init__(self, spisok: {}):
        self.spisok = spisok


class ProductStorage:
    def __init__(self, name: str, storage: [Product]):
        self.name = name
        self.storage = storage