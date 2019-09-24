import json  # imports the json package so we can use it in our code
from my_classes import Hitting  # standard way to import our own class from another file in our project
# from .my_classes import Hitting  # same as above, but based on dot, so relative to current file location
# from . import my_classes  # import the whole file from the same folder, then you would need to use my_classes.Hitting
# from .. import stuff  # import a file from a parent directory
# from ... import blah  # import a file from the "grandparent" directory

my_dict = {  # standard example dictionary
    'a': 1,
    'b': 2,
}
print(json.dumps(my_dict))  # json.dumps (dump to string) turns it into this:
# '{"a": 1, "b": 2}'  # changes all strings to use double-quotes and standardizes spacing

my_list = ['a', 'b', 'c', 1, 3, 5]  # standard example list
print(json.dumps(my_list))
# '["a", "b", "c", 1, 3, 5]'  # strings get ", numbers have no punctuation

my_tuple = ('a', 'b', 'c', 2, 4, 6)  # standard example tuple
print(json.dumps(my_tuple))
# '["a", "b", "c", 2, 4, 6]'  # json doesn't have a tuple, so it uses a list

my_set = {'a', 'b', 'c', 1, 2, 4, 'a'}  # standard example set
# {1, 2, 4, 'c', 'a', 'b'}  # remember that the set removes duplicates and ordering
print(json.dumps(list(my_set)))  # json will not encode a set, so we change it to a list
# '[1, 2, 4, "c", "a", "b"]'

jones = Hitting() # make an instance of our class Hitting
print(json.dumps(str(jones))) # Hitting is not known to the json encoder, but string is
# "0 0 0"
