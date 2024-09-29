class Product:
    def __init__(self, name:str, cost:float, weight:float, count:int, quality:float):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.count = count
        self.quality = quality
    def __str__(self):
        return self.name + " стоят: " + str(self.cost) + " рублей за: " + str(self.weight) + " кг, в упаковке: " + str(self.count) + " пельменей. Качество товара: " + str(self.quality) + " из 5"

a = [Product("Говяжьи пельмени от Андрея", 599.99, 0.9, 50, 5),
Product("Пельмени из Свинины от Андрея", 549.99, 0.9, 50, 5),
Product("Пельмени от Андрея", 549.99, 0.9, 50, 5)]