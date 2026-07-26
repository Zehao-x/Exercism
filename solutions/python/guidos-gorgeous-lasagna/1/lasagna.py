"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
layer_time = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: the remaining time

    function to calculate how many minutes the lasagna still needs to bake based on the `EXPECTED_BAKE_TIME` constant.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time

    return remaining_bake_time
    



def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): the total number of layers you want to add to lasagna
    Returns:
        int: the total time you spend on the layers

    function to calculate you want to add to the lasagna as an argument and returns how many minutes you would
    spend making them.
    """

    return number_of_layers * layer_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed  time in minutes

    Parameters:
        number_of_layers (int): the total number of layers you want to add to lasagna
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: the total time you spend in the ketchen cooking

   This function should return the total minutes you have been in the kitchen cooking — your preparation time 
   layering + the time the lasagna has spent baking in the oven.
    """
    
    prep_time = preparation_time_in_minutes(number_of_layers)

    return prep_time + elapsed_bake_time

