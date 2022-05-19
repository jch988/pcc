from new_section import new_section as ns

# 9-10

from restaurant import Restaurant as Rs

taco_truck = Rs('Tacos on Wheels', 'breakfast tacos')
taco_truck.describe_restaurant()

ns()

# 9-11 Imported Admin

from imported_admin import User, Admin, Privileges
new_admin = Admin('vladmir', 'putin', 'isuckdicks', 'childmolester')
new_admin.privileges.show_privileges()

ns()

# 9-12 Mulitple Modules

from admin import Admin, Privileges
from user import User

another_admin = Admin('Tony', 'Stark', 'ironman', 'snap')
another_admin.privileges.show_privileges()