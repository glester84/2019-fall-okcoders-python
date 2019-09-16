# Self, Stars, and Comprehensions

## Week 3 objective
1. Review json encoding (carry-over from week 2).
1. Review pep8 style linter (carry-over from week 2).
1. Understand the difference between a class and its instances.
1. Be able to apply "self" when appropriate.
1. Use default values for arguments
1. Use argument list (*args)
1. Use keyword arguments (**kwargs)
1. Read and write list comprehensions
1. Read and write dictionary comprehensions

## JSON encoding
`import json`
`json.loads()` -> load a string into an object
`json.dumps()` -> dump an object to a string
Cases where `my_obj != json.loads(json.dumps(my_obj))`

## Pep8
`pep8 baseball.py` -> lint a single file
`pep8 *.py` -> lint all files matching wildcard
`pep8 .` lint a directory and all subdirectories

## Class vs. Object and when to use "self"
A class definition says what a class is and what it can do.
An object actually is that thing and can perform its actions.
If a class "method" needs to work on the data, use self.
If a class "function" doesn't, self is not necessary.

## Arguments with names and defaults
-arguments defaults go after required arguments on definition
-arguments with names go after positional arguments when calling

## Star Arguments / Parameters
`*args` means any number of parameters without names
-must be after all "formal" parameters on definition
-treated as a list
-can be empty
`**kwargs` means any number of parameters with names
-must be the last parameter on definition
-can be applied to the call in any order after all positional arguments

## List Comprehensions
Builds a list by applying some code to all items in something iterable
-seems pretty simple but can be combined with other concepts to make powerful and/or complicated code
-actually very efficient
simple -> `names = [item.name for item in list_of_objects]`
interesting -> `test_scores = [test.correct / test.total for test in graded_tests]`
with condition(s) -> `qualified_values = [val for val in [1, 2, 3, 4, 5] if val > 2]`
maybe too much -> `unwrapped = [val for group in [[1, 2, 3], [4, 5, 6]] for val in group]`
definitely too much -> `filtered = [val for group in [[1, 2, 3], [4, 5, 6]] if sum(group) > 10 for val in group]`

## Dictionary Comprehensions
Builds a dictionary by applying some code to all items in something iterable
-seems complex, but is basically the same as list comprehensions
simple -> `names = {item.name: item for item in list_of_objects}`
interesting -> `test_scores = {test.student: test.correct / test.total for test in graded_tests}`
...
