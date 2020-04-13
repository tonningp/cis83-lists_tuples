import random
from faker import Faker

def random_name_list(num):
    return [Faker().first_name() for i in range(num)]

def random_name_tuple(num):
    # this is an example of a list comprehension
    return [Faker().first_name() for i in range(num)]

def random_name():
    return Faker().first_name()