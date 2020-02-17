def map_tuple(func, tup):
    new_tuple = ()
    for each in tup:
        new_tuple += (func(each),)
    return new_tuple


