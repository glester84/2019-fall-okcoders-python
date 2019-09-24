# structure of a basic list comprehension
names = [item.name for item in list_of_objects]
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

# the "first thing" can be an expression with many parts
test_scores = {test.student: test.correct / test.total for test in graded_tests}
# looking inside the curly braces
test.student: test.correct / test.total for test in graded_tests
# moving the first item inside
for test in graded_tests:
    test.student: test.correct / test.total
# viewing as a function
def student_score(graded_tests):
    student_scores = {}
    for test in graded_tests:
        student_scores[test.student] = test.correct / test.total
    return student_scores

# comprehensions can have for and if together
qualified_values = [val for val in [1, 2, 3, 4, 5] if val > 2]
# first look inside the brackets
val for val in [1, 2, 3, 4, 5] if val > 2
# then move the first thing inside the rest
for val in [1, 2, 3, 4, 5]:
    if val > 2:
        val
# view as a function
def do_stuff(objs):
    return_me = []
    for val in objs:
        if val > 2:
            return_me.append(val)
    return return_me

# comprehensions can also have for and for nested together
unwrapped = [val for group in [[1, 2, 3], [4, 5, 6]] for val in group]
# look inside the brackets
val for group in [[1, 2, 3], [4, 5, 6]] for val in group
# move the first item inside the rest
for group in [[1, 2, 3], [4, 5, 6]]:
    for val in group:
        val
# view as a function
def funct(things):
    items = []
    for group in things:
        for val in group:
            items.append(val)
    return items

# an example of for..if..for
filtered = [val for group in [[1, 2, 3], [4, 5, 6]] if sum(group) > 10 for val in group]
# look inside the brackets
val for group in [[1, 2, 3], [4, 5, 6]] if sum(group) > 10 for val in group
# move the first item inside and nest the rest
for group in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    if sum(group) > 10:
        for val in group:
            val
# view as a function
def get_filtered(list_of_groups):
    values = []
    for group in list_of_groups:
        if sum(group) > 10:
            for val in group:
                values.append(val)
    return values

# now can we tell what would happen in this case?
get_filtered([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#possibility #1
[[4, 5, 6], [7, 8, 9]]
#possibility #2
[4, 5, 6, 7, 8, 9]

# the correct answer is #2 as written...
# we could change to #1 by returning the group instead of looping over it
def get_filtered(list_of_groups):
    values = []
    for group in list_of_groups:
        if sum(group) > 10:
            values.append(group)
    return values
# and then look at just the nested items and value
for group in list_of_groups:
    if sum(group) > 10:
        group
# and roll up onto one line with the value first
group for group in list_of_groups if sum(group) > 10
# finally put brackets around it and assign to a variable
filtered_groups = [group for group in list_of_groups if sum(group) > 10]
