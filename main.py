import random
# import from other files
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_decimal = random.random() * 10
print(random_decimal)

random_score = random.randint(0, 100)
print(random_score)

# import from other files
print(my_module.pi)