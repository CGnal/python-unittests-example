

class Calculator:
    def __init__(self):
        pass

    def add(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a: int, b: int) -> int:
        return a - b

    def mul(self, a: int, b: int) -> int:
        return a * b

    def div(self, a: int, b: int) -> float:
        if b == 0:
            raise ZeroDivisionError("The divisor must not be zero")
        return a / b
