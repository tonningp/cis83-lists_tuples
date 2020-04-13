'''
examples of how lists are manipulated and used
in python programs
'''
import utils

def lists_as_sequences():
    # lists are sequences
    # To create an empty list, use this assignment
    my_list = []
    # because string is an iterable, it will become a
    # list of characters, looks at the following
    my_list += 'Hello';
    print(my_list)
    # it should print ['H', 'e', 'l', 'l', 'o']

def lists_can_contain_other_lists():
    my_list = [] # create an empty list
    # lists can also have other lists as one of the items
    my_list += [['one','two','three'],'orange','red']
    print(my_list)

def lists_are_mutable(): 
    my_list = utils.random_name_list(5) # creates a new list of random names
    # lists are mutable, this means that the list elements can be changed.
    print(f'list -> before change:\n {my_list}')
    my_list[0] = utils.random_name()
    print(f'list -> after change:\n {my_list}')