# %%
# the function takes a list of numbers and returns the sum of all the numbers in the list
# positional arguments *args
# Checkpoint 1 
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

# Checkpoint 2 
def assign_and_print_order(table_number, *order_items):
   # Checkpoint 3
  tables[table_number]['order'] = order_items
  # Checkpoint 4
  for order_item in order_items:
    print(order_item)


# Checkpoint 5
assign_table(2, 'Arwa', True)

# Checkpoint 6
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables)

# %%
# keyword arguments **kwargs
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

# Write your code below: 
def assign_food_items(**order_items):
  print(order_items)

  food = order_items.get('food')
  drinks = order_items.get('drinks')
  print(food)
  print(drinks)
  
# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')


# %%
# keyword arguments **kwargs
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

print('\n --- tables after update --- \n')
assign_food_items(2, food = 'Seabass, Gnocchi, Pizza', drinks = 'Margarita, Water')

print(tables)


# %%
# Checkpoint 1 & 2
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)


# Checkpoint 3 (keyword names are arbitrary for desert_scoops)
single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides='Mashed Potatoes', ice_cream_scoop1='Vanilla', ice_cream_scoop2='Cookies and Cream' )


# %%
# unpacking operator * and **
order = ['Baby Beets', 'Salmon', 'Scallops']
single_prix_fixe_order(*order, sides='Mashed Potatoes', ice_cream_scoop1='Vanilla', ice_cream_scoop2='Cookies and Cream' )


# %%
# built-in functions > global scope > enclosing scope > local scope
print(dir(__builtins__))


#%%
# global scope
# nested names will not be accessible in the global scope
print(' -- Globals Namespace with empty script -- \n')
# Write Checkpoint 1 here: 
print(globals())

# Write Checkpoint 2 here: 
global_variable = 'global'

# Write Checkpoint 3 here: 
def print_global():
  global_variable = 'nested global' # this is a local variable(nested)
  nested_variable = 'nested value'  # this is a local variable(nested)

print(' \n -- Globals Namespace non-empty script -- \n')

# Write Checkpoint 4 here: 
print(globals())


# %%
global_variable = 'global'

print(' -- Local and global Namespaces with empty script -- \n')

# Write Checkpoint 1 here:
print(locals())
print(globals())

# Write Checkpoint 2 here:
def divide(num1, num2):
  result = num1 / num2
  print(locals())

# Write Checkpoint 3 here:
def multiply(num1, num2):
  product = num1 * num2
  print(locals())


print(' \n -- Local Namespace for divide -- \n')

# Write Checkpoint 4 here:
divide(3, 4)

print(' \n -- Local Namespace for multiply -- \n')

# Write Checkpoint 5 here:
multiply(4, 50)

print(' \n -- Local Namespace final -- \n')

# Write Checkpoint 6 here:
print(locals())


# %%
# enclosing scope
global_variable = 'global'
 
def outer_function():
  outer_value = "outer"
 
  def inner_function():
    inner_value = "inner"

    def inner_nested_function():
      nested_value = 'nested'
    inner_nested_function()
    # Add locals() below
    print(locals())
    
  inner_function()
 
outer_function()


# %%
# Enclosing/Nonlocal Scope
def calc_paint_amount(width, height):

  square_feet = width * height
  # Write your code below!
  def calc_gallons():
    return square_feet / 400
  
  return calc_gallons()

print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))


# %%
# nonlocal scope
walls = [(20, 9), (25, 9), (20, 9), (25, 9)]


def calc_paint_amount(wall_measurements):

  square_feet = 0

  def calc_square_feet():
    nonlocal square_feet # nonlocal keyword
    
    for width, height in wall_measurements:
      square_feet += width * height

  def calc_gallons():
    return square_feet / 400

  calc_square_feet()

  return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))


# %%
# global scope
paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
}

def print_available(color):
  #   paint_gallons_available = { # local scope should not be defined
  #     'red': 50,
  #     'blue': 72,
  #     'green': 99,
  #     'yellow': 33
  # }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


def print_all_colors_available():
  for color in paint_gallons_available:
    print(color)

print_available('red')
print_all_colors_available()


# %%
# Or use the global keyword
def print_available(color):
  global paint_gallons_available
  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


print_available('red')
for color in paint_gallons_available:
  print(color)
  
  """
  Remember the LEGB rule: Local, Enclosing, Global, Built-in. The global keyword allows you to modify the global variable from within the function. However, it is generally better to avoid using global variables in functions, as it can make the code harder to understand and maintain. Instead, you can pass the variable as an argument to the function, or return the variable from the function.
  
  Higher-order functions. To summarize, we learned:

  1. Higher-order functions are possible because functions are first-class objects in Python, meaning that a function can be stored as a variable, passed as an argument to a function, returned by a function, and stored in data structures (lists, dictionaries, etc.).
  2. Higher-order functions are functions that operate on other functions by taking another function as an argument, returning another function, or both.
  3. Higher-order functions can reduce repetition in code, making code easier to read and less prone to mistakes.
  """
  
# %%

age = 27 

def func(): 

  def inner_func():
    print(age)
  inner_func()

func()


# %%
# Higher-order functions: map, filter, reduce!!
# The map() higher-order function has the following base structure:
# returned_map_object = map(function, iterable)

def double(x):
 return x*2
 
int_list = [3, 6, 9]
 
doubled = map(double, int_list)
 
print(doubled) # <map object at 0x7f3e3c6b3a90>
print(list(doubled)) # [6, 12, 18]

# %%
# The filter() higher-order function has the following base structure:
# returned_filter_object = filter(function, iterable)
# The filtering function should be a function that returns a boolean value: True or False.
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
 
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names) 
 
print(M_names) # <filter object at 0x7f3e3c6b3a90>
print(list(M_names)) # ['margarita', 'Masako', 'Maki']

# %%
# The reduce() higher-order function has the following base structure:
# returned_reduce_object = reduce(function, iterable)
from functools import reduce
 
int_list = [3, 6, 9, 12]
 
reduced_int_list = reduce(lambda x,y: x*y, int_list)
 
print(reduced_int_list) # 1944


# %%
# Abstract Base Classes
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    new_id = 1
    
    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass

class Employee(AbstractEmployee):
    def say_id(self):
        print(f"My ID is {self.id}")

e1 = Employee()
e1.say_id()

# %%
from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Even if you implement the abstract methods in AbstractShape, you can't instantiate it
class ConcreteShape(AbstractShape):
    def area(self):
        return 0  # Dummy implementation

    def perimeter(self):
        return 0  # Dummy implementation

# Trying to instantiate AbstractShape will raise an error
# abstract_shape = AbstractShape()  # TypeError: Can't instantiate abstract class AbstractShape

# Instantiating ConcreteShape is allowed because it provides specific implementations of the abstract methods
concrete_shape = ConcreteShape()  # This is valid



# %%
# Multiple Inheritance
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Write your code below
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, "Admin")

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()


# %%
# Dunder Methods
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  def __len__(self):
    return len(self.attendees)
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()

m1 + e1
m1 + e2
m1 + e3
print(len(m1))


# %%
# Encapsulation
class Employee:
    def __init__(self):
        self.id = 1  # Public attribute

emp = Employee()
print(emp.id)  # Accessible from outside


class Employee:
    def __init__(self):
        self._id = 1  # Protected attribute

emp = Employee()
print(emp._id)  # Accessible, but should be avoided as per convention


class Employee:
    def __init__(self):
        self.__id = 1  # Private attribute

emp = Employee()
# print(emp.__id)  # This will raise an AttributeError
print(emp._Employee__id)  # This is the way to access it, but should be avoided



# %%
# Getter, Setter, and Deleter
class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  # Write your code below
  def get_name(self):
    return self._name

  def set_name(self, _name):
    self._name = _name

  def del_name(self):
    del self._name

e1 = Employee("Maisy")
e2 = Employee()



e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name())


# %%
# School Catalogue Exercise

class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def set_numberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return f"{self.level} scholl named {self.name} with {self.numberOfStudents} students"

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'Primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f"The pickup policy is {self.pickupPolicy}."

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f"The sports team is {self.sportsTeams}."

a = School("Codecademy", "high", 100)
print(a)
print(a.get_name())
print(a.level)
a.set_numberOfStudents(200)
print(a.numberOfStudents)

print()

b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.get_pickupPolicy())
print(b)

print()

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_sportsTeams())
print(c)


# %%
# Built-in property function
# Instead of using getters and setters, we can use the property function to create properties for our class.
# This helps us to avoid the use of getters and setters and makes the code more readable.
class Box:
  def __init__(self, weight):
    self.__weight = weight

  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight

  def delWeight(self):
    del self.__weight

  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")
  
box = Box(10)
print(box.weight) #this calls .getWeight()
box.weight = 5 #this called .setWeight()
del box.weight #this calls .delWeight()
box.weight = -5 #box.__weight is unchanged 


# %%
# @property decorator
class Box:
 def __init__(self, weight):
   self.__weight = weight

 @property
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight

 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight

 @weight.deleter
 def weight(self):
   del self.__weight
   
box = Box(10)
print(box.weight)
box.weight = 5
del box.weight


# %%
   """
   The full heirarchy of built-in exceptions as follows:
   
   BaseException
    +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
          |    +-- ModuleNotFoundError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
   """
   
instrument_catalog = {
  'Marimba': 1999,
  'Kora': 499,
  'Flute': 899
}

def print_instrument_price(instrument):
    # Checkpoint 2
    if instrument in instrument_catalog:
      print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
    # Checkpoint 3
    else:
      raise KeyError(instrument + ' is not found in instrument catalog!')

# def print_instrument_price(instrument):
#   # Write your code below:
#   if instrument in instrument_catalog:
#     print(f"The price of {instrument} is {instrument_catalog[instrument]}")
#   else:
#     raise KeyError(f"{instrument} is not found in {instrument_catalog}")


print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')


# %%
# Exception Handling
# try, except, else, finally
# Checkpoint 1
staff = {
  'Austin': {
      'floor managers': 1,
      'sales associates': 5
  },
  'Melbourne': {
      'floor managers': 0,
      'sales associates': 8
  },
  'Beijing': {
      'floor managers': 2,
      'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  # Checkpoint 2
  try:
    print_staff_report(location, staff)
  # Checkpoint 3
  except ZeroDivisionError as  e:
      print('Could not print sales report for ' + location)
      print('We hit a ZeroDivisionError')
      print(e)
      print()


# %%
# Handling Multiple Exceptions
# Checkpoint 1
instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Banjo'
discount = 20

# Checkpoint 2
try:
  display_discounted_price(instrument, discount)
# Checkpoint 3
except KeyError:
  print('An invalid instrument was entered!')
# Checkpoint 4
except TypeError:
  print('Discount percentage must be a number!')
except Exception:
  print('Hit an exception other than KeyError or TypeError!')
  

# %%
# The Else Clause
# To run some code only if we do not encounter an exception
# Checkpoint 1
customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
  # Checkpoint 2
  try:
    rewards_number = customer_rewards[customer]
  except KeyError:
    print('Customer was not found in rewards program!')
  # Checkpoint 3
  else:
    print('Rewards account number is: ' + str(rewards_number)) # this will only run if no exception is raised

# Checkpoint 4
customer = 'Mario'
display_rewards_account(customer)


# %%
# The Finally Clause
# To run some code regardless of whether an exception was raised
# Checkpoint 1
customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
  # Checkpoint 2
  try:
    rewards_number = customer_rewards[customer]
  except KeyError:
    print('Customer was not found in rewards program!')
  # Checkpoint 3
  else:
    print('Rewards account number is: ' + str(rewards_number)) # this will only run if no exception is raised
  finally:
    print('Thank you for checking your rewards account!') # this will always run

# Checkpoint 4
customer = 'Mario'
display_rewards_account(customer)


# %%
# User-Defined Exceptions
# Checkpoint 1
inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

# Checkpoint 2
class InventoryError(Exception): # create a custom exception. It should inherit from the Exception class
  pass

def submit_order(instrument, quantity):
  supply = inventory[instrument]
  
  # Checkpoint 3
  if quantity > supply:
    raise InventoryError
  # Checkpoint 4
  else:
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)


# %%
# Customizing User-Defined Exceptions
class InventoryError(Exception):
  def __init__(self, supply):
    self.supply = supply

  def __str__(self):
    return 'Available supply is only ' + str(self.supply)

inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

def submit_order(instrument, quantity):
  supply = inventory[instrument]
  if quantity > supply:
    raise InventoryError(supply)
  else:
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)


# %%
# Assert Statements
destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'

assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'

city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)


# %%
# Unit Testing
def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

# Write your code below:
def test_row_1():
  assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'

def test_row_20():
  assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'

def test_row_40():
  assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back!'

test_row_1()
test_row_20()
test_row_40()


# %%
# Unit Testing with unittest
# your code below:
import unittest

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

# Write your code below:
class NearestExitTests(unittest.TestCase):
  def test_row_1(self):
   self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')

  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20),'middle', 'The nearest exit to row 20 is in the middle!')

  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40),'back', 'The nearest exit to row 40 is in the back!')

unittest.main()
# %%
# Assert Statements: assertEqual, assertNotEqual, assertTrue, assertFalse, assertIn, assertNotIn
import unittest
from unittest import entertainment 

# Write your code below: 
class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

unittest.main()

# %%
import unittest
from unittest import entertainment 

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Write your code below:
  def test_maximum_display_brightness(self):
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)

  def test_device_temperature(self):
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)

unittest.main()

# %%
import unittest
from unittest import alerts

# Checkpoint 1
class SystemAlertTests(unittest.TestCase):
    
  # Checkpoint 2
  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)
    
  # Checkpoint 3
  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)

unittest.main()


# %%
import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movies = entertainment.get_daily_movies()
    licensed_movies = entertainment.get_licensed_movies()

    # Write your code below:
    for movie in daily_movies:
      print(movie)

    self.assertIn(daily_movies, licensed_movies)

unittest.main()

# %%
import unittest
from unittest import entertainment 

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    # Checkpoint 1
    daily_movies = entertainment.get_daily_movies()
    licensed_movies = entertainment.get_licensed_movies()

    # Checkpoint 2
    for movie in daily_movies:
      print(movie)
      # Checkpoint 3 & 4
      with self.subTest(movie):
        self.assertIn(movie, licensed_movies)


unittest.main()

# %%
# setUp and tearDown
# Checkpoint 1
import unittest
from unittest import kiosk


class CheckInKioskTests(unittest.TestCase):

  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  # Checkpoint 2
  @classmethod
  def setUpClass(cls):
    kiosk.power_on_kiosk()
    
  # Checkpoint 3
  @classmethod
  def tearDownClass(cls):
    kiosk.power_off_kiosk()
    
  # Checkpoint 4
  def setUp(self):
    kiosk.return_to_welcome_page()

unittest.main()


# %%
# Skippping Tests
import unittest
from unittest import entertainment
import sys

class EntertainmentSystemTests(unittest.TestCase):
  # Checkpoint 1
  @unittest.skipIf(entertainment.regional_jet(), 'Not available on regional jets')
  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  # Checkpoint 2
  @unittest.skipUnless(entertainment.regional_jet() is False, 'Not available on regional jets')
  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Checkpoint 3
  def test_device_temperature(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)

  # Checkpoint 3
  def test_maximum_display_brightness(self):
    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)


unittest.main()


# %%
# Expected Failures
import unittest
import feedback

class CustomerFeedbackTests(unittest.TestCase):

  # your code below:
  @unittest.expectedFailure # this test is expected to fail
  def test_survey_form(self):
    self.assertEqual(feedback.issue_survey(), 'Success')
    # raise Exception('This test is expected to fail')

  def test_complaint_form(self):
    self.assertEqual(feedback.log_customer_complaint(), 'Success')

unittest.main()


# %%
# Custom Iterators
class Counter:
  def __init__(self, start, end):
    self.current = start
    self.end = end

  def __iter__(self):
    return self

  def __next__(self):
    if self.current > self.end:
      raise StopIteration
    else:
      self.current += 1
      return self.current - 1

for num in Counter(1, 5):
  print(num)
  
  
# %%
class CustomerCounter:
  
    # def __init__(self, ):
    #   self.count = 

  def __iter__(self):
    self.count = 0
    return self

  def __next__(self):
    self.count += 1

    if self.count > 100:
      raise StopIteration
    return self.count

customer_counter = CustomerCounter()

for customer_count in customer_counter:
  print(customer_count)
  
# %%
# Itertools: Built-in Iterators: Infinite Iterators, Input-dependent Iterators, Combinatoric Iterators
# Infinite Iterators: count, cycle, repeat
import itertools

max_capacity = 1000
num_bags = 0

for i in itertools.count(start = 13.5, step = 13.5):
  if i >= max_capacity:
    break
  num_bags += 1

print(num_bags)


# %%
# Input-dependent Iterators: takewhile, dropwhilem, chain
import itertools
great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

# Write your code below: 
all_skus_iterator = itertools.chain(great_dane_foods, min_pin_pup_foods, pawsome_pup_foods)
print(all_skus_iterator)

for i in all_skus_iterator:
  print(i)


# %%
# Combinatoric Iterator: Combinations, Permutations, Product
import itertools
collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

# Write your code below: 
collar_combo_iterator = itertools.combinations(collars, 3)
print(collar_combo_iterator)
print()

collar_combo_iterator_list = list(collar_combo_iterator)
print(collar_combo_iterator_list)
print()

for i in collar_combo_iterator:
  print(i)


# %%
import itertools

cat_toys = [("laser", 1.99), ("fountain", 5.99), ("scratcher", 10.99), ("catnip", 15.99)]
cat_toy_iterator = iter(cat_toys)
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))


max_money = 15
options = []

toy_combos = itertools.combinations(cat_toys, 2)

for combo in toy_combos:
   toy1 = combo[0]
   cost_of_toy1 = toy1[1]
   toy2 = combo[1]
   cost_of_toy2 = toy2[1]
   if cost_of_toy1 + cost_of_toy2 <= max_money:
    options.append(combo)

print(options)

# %%
def class_standing_generator():
  yield 'Freshman'
  yield 'Sophomore'
  yield 'Junior'
  yield 'Senior'

def class_standing_generator1():
  return 'Freshman'
  return 'Sophomore'
  return 'Junior'
  return 'Senior'

class_standings = class_standing_generator()
class_standings1 = class_standing_generator1()

for class_standing in class_standings:
  print(class_standing)

for class_standing in class_standings1:
  print(class_standing)
  

# %%
def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
  # Write your code below:
  for student in student_standings:
    if student == 'Freshman':
      yield 500

standing_values = student_standing_generator()

print(next(standing_values))
print(next(standing_values))
print(next(standing_values))


# %%
# Generator object
def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)

# Checkpoint 1
cs_courses = cs_generator() # this is a generator object
for course in cs_courses:
  print(course)

# Checkpoint 2
cs_generator_exp = ("Computer Science {}".format(i) for i in range(1,5)) # similar to list comprehension [] -> ()

# Checkpoint 3
for course in cs_generator_exp:
  print(course)
  
  
# %%
