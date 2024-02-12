# Printing 3D models
def print_models(unprinted_designs, completed_models):
    """ 
    Simulates printing each design, until none are left
    Move  each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing the model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all completed models """
    print("\nThe following models have been completed: ")
    for completed_model in completed_models:
        print(completed_model)