def lists_as_sequences():
    # lists are sequences
    # To create an empty list, use this assignment
    my_list = []
    # because string is an iterable, it will become a
    # list of characters, looks at the following
    my_list += 'Hello';
    print(my_list)
    # it should print ['H', 'e', 'l', 'l', 'o']
    # lists can also have other lists as one of the items
    my_list += [['one','two','three'],'orange','red']
    print(my_list)
    
    # lists are mutable, this means that the list elements can be changed.
    my_list[0] = 'Changed Item'
    print(my_list)
