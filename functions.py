def greet(name):
    print("Hello "+name)

def greet_name(name):
    print(f"Hello {name}")

def details(last_name,first_name="John"):
    print(first_name +" "+last_name)

greet('darshan')
greet_name('David')
details(last_name='David')


def calculate_total(price):
    tax_rate = 0.08
    tax = price*tax_rate
    final_price = price+tax-10
    print(f"Total Price: {final_price}")

calculate_total(100)


def simple_function():
    numbers=[1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number,last_number


last , first = simple_function()

first



