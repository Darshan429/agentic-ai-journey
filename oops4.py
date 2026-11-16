class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        return f"{self.name} is sleeping"

    def eat(self):
        return f"{self.name} is eating"


class Dog(Animal):
    def bark(self):
        return f"{self.name} say's woof!"


my_dog = Dog("buddy")
my_dog.sleep()
my_dog.eat()
my_dog.bark()


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 6},
    {"name": "banana", "price": 0.3, "quantity": 8},
]
print(calculate_total(shopping_cart))





