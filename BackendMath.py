class BackendMath:

    def __init__(self):
        self.a = 0
        self.b = 0

    def add(self, a, b):
        self.a = a
        self.b = b
        return a + b

    def subtract(self, a, b):
        self.a = a
        self.b = b
        return a - b

    def multiply(self, a, b):
        self.a = a
        self.b = b
        return a * b

    def divide(self, a, b):
        self.a = int(a)
        self.b = int(b)
        if a == 0:
            print("Деление на ноль - Невозможно")
        elif b == 0:
            print("Деление на ноль - Невозможно")
        else:
            return a / b
