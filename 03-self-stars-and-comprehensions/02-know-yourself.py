# define a function with no arguments outside of a class
def my_func():
    return 'a'

# call the function with parens and nothing else required
my_func()  # returns 'a'

# define a function with some arguments outside of a class
def my_adder(a,b):
    return a+b

# call the function with only the arguments
my_adder(5, 1)  # returns 6

# create a class and put some functions and data inside it
class Car:
    value = 10000
    gas = 0
    octane = 0

    # define a function that takes no "arguments" (except self)
    def get_value(self):
        return self.value

    # define a function that takes an argument (in addition to self)
    def set_value(self, new_value):
        self.value = new_value

    # define a function without a self attribute
    def base_value():
        # we can not use self.value here, only Car.value
        return Car.value

    # define a function with some default arguments and "star args" for a list of optional arguments
    def fill_with_gas(self, amount=100, octane=89, *args):
        self.gas = amount
        self.octane = octane

    # define a function with some keyword arguments
    def air_up_tires(self, **kwargs):
        """
        Sets the value of all the tire pressure
        maybe returns the difference between recommended pressure and what you supplied
        """
        print(kwargs)

# make an instance of Car (the class) and call it my_car (the object)
my_car = Car()
print(f'{my_car.gas} {my_car.octane} {my_car.value}')
# initial values of 0, 0, 10000

my_car.set_value(9999)  # my_car->self, 9999-> new_value
my_car.get_value()  # my_car-> self... returns 9999
Car.get_value(my_car)  # exact same function is called... returns 9999

Car.base_value() # still returns 10000
# my_car.base_value()  # doesn't work because we provided an argument my_car that had no place to go

# calling functions on objects makes the object the first argument
# i.e. my_car -> self
my_car.fill_with_gas() # uses default values to set gas=100, octane=89
my_car.fill_with_gas(amount=70) # uses default values only for the values that aren't specified
# results in gas=70, octane=89
my_car.fill_with_gas(octane=93, amount=my_car.gas) # we would need to do this if we don't want the default values to be used
# results in gas=70, octane=93
my_car.fill_with_gas(50) # if no names are provided, values fill from the left
# results in gas=50, octane=89
my_car.fill_with_gas(100, 91, 5, 10, 15) # extra non-keyword arguments go into *args
# results in gas=100, octane=91, args=[5, 10, 15]
# my_car.fill_with_gas(octane=91, 1, 2, 3) # we can't put positional args after named ones

# keyword arguments are optional
my_car.air_up_tires()  # prints an empty dictionary
# car.air_up_tires(34, 34, 34, 34)  # doesn't work because kwargs (**keyword args) require keywords
my_car.air_up_tires(front_left=35, front_right=28, rear_left=48, rear_right=28)
# prints {'front_left': 35, 'front_right': 28, 'rear_left': 48, 'rear_right': 28}
