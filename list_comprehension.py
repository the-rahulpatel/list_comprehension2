import random


def list_comprehension():
    a = random.sample(range(10), 9)
    b = random.sample(range(10), 6)
    new_list = [i for i in set(a) & set(b)]
    print(new_list)

list_comprehension()
