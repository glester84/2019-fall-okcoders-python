# structure of a basic list comprehension
names = [item.name for item in list_of_objects]

names = (item.name for item in list_of_objects)

# to understand, first look inside brackets
item.name for item in list_of_objects
# then move the first thing inside the rest
for item in list_of_objects:
    item.name
# finally convert to a function
def comprehend_list(list_of_objects):
    names = []
    for item in list_of_objects:
        names.append(item.name)
    return names

# same example as a generator
item.name for item in list_of_objects
# re-structure the code in the same way as before
for item in list_of_objects:
    item.name
# yield the values as you see them
def generate_names(list_of_objects):
    for item in list_of_objects:
        yield item.name




# similar example as a dictionary comprehension
names = {item.name: item for item in list_of_objects}
# to understand, first look inside curly braces
item.name: item for item in list_of_objects
# then move the "evaluation" inside the rest
for item in list_of_objects:
    item.name: item
# finally convert to a function
def comprehend_dictionary(list_of_objects):
    names = {}
    for item in list_of_objects:
        names[item.name] = item
    return names


my_stuff = ['a', 'b', 1, 3, 6]
my_things = ('a', 'b', 1, 3, 6)
my_objects = {'a', 'b', 1, 3, 6}
my_stuff[0]


names = ({item.name, item} for item in list_of_objects)

for item in list_of_objects:
    {item.name, item}

def names_of_things(list_of_objects):
    for item in list_of_objects:
        yield {item.name, item}
