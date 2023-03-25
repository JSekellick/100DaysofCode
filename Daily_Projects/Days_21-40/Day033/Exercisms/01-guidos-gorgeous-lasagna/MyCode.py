"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#TODO: define the 'EXPECTED_BAKE_TIME' constant.

EXPECTED_BAKE_TIME = 40
"""Added 40 minutes from reference import lasagna"""

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.

def bake_time_remaining(elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - time remaining (in minutes) until food is complete.

    This function takes two integers. The time required to cook and the time elapsed in cooking.
    The elapsed time is subtracted from total time required.

    EXPECTED_BAKE_TIME of the item is always constant per the cookbook
    """

    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time

#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.

def preparation_time_in_minutes(number_of_layers):
    """The number of layers is based on the user input. 
    Preparation time is is based on the number of layers muliplied 2 minutes for each layer
    """
    preparation_time = (number_of_layers * 2)
    return preparation_time

#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time spent so far including preparation.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.

    EXPECTED_BAKE_TIME of the item is always constant per the cookbook
    """
    time_elapsed = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return time_elapsed
