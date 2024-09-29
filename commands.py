import classes

class AddCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        self.productStorage.storage.append(classes.Product(params[0], params[1], params[2], params[3], params[4]))

class ListCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        for x in range(len(self.productStorage.storage)):
            print(x, "." + str(self.productStorage.storage[x]))

class RemoveCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        self.productStorage.storage.pop(int(params[0]))

class HelpCommand:
    def __init__(self, command_d):
        self.command_d = command_d

    def execute(self, params: []):
        self