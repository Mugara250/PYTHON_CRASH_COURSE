#!/usr/bin/python3
# import printing_functions as pf # Importing the whole module as an alias

# # Calling the function using the imported module
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# pf.print_models(unprinted_designs, completed_models)
# pf.show_completed_models(completed_models)

# Importing specific functions from a module as aliases
from printing_functions import print_models as pm, show_completed_models as scm # OR
# Importing all functions within the module
from printing_functions import *
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm(unprinted_designs, completed_models)
scm(completed_models)