# Importing classes

# import a single class from a module
from car_module import Car

# aliases work, too
from car_module import ElectricCar as EC

# import multiple classes from a module
from car_module import Car as C, ElectricCar as EC

# import entire module and use dot notation
import car_module as cars
my_tesla = cars.ElectricCar('tesla', 'roadster', 2019)

# import a module into another module
	# necessary if you have related modules spread across multiple files
	# still need to import relevant parents into main file


# when importing a class from a file that contains other code (like
# instances), the rest of the code ets run. Idk why that is or how
# to stop it

# seems like the module I'm iporting from must only contain the class
# and relating methods, not instances or mainline code