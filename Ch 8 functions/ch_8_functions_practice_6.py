from new_section import new_section as ns

ns()

# 8-15 Printing Models

import ch_8_functions_practice_printing_functions as printing

unprinted_designs = ['book cover', 'jacket', 'viruses']
completed_models = []

printing.print_models(unprinted_designs, completed_models)
printing.show_completed_models(completed_models)


ns()


# 8-16 Imports

# import sandwich
# from sandwich import make_sandwich
# from sandwich import make_sandwich as make
# import sandwich as sw
from sandwich import *

make_sandwich('wheat', 'turkey', 'swiss', 'mustard', 'avocado')

