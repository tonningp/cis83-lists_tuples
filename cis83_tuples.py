import utils
def tuples_are_immutable():
    t1 = utils.random_name_tuple(5)
    # tuples are not mutable
    # uncomment the following code and there 
    # will be a syntax error when this function
    # is called
    t1[0] = 10
    return t1