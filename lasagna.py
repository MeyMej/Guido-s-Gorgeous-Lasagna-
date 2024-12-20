"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
"""Define the EXPECTED_BAKE_TIME constant that represents how many minutes the lasagna should         
bake in the oven. According to your cookbook, the Lasagna should be in the oven for 40 minutes:
"""
EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
"""Complete the bake_time_remaining() function that takes the actual minutes the lasagna has         
been in the oven as an argument and returns how many minutes the lasagna still needs to               
bake based on the EXPECTED_BAKE_TIME constant."""
def bake_time_remaining(minutes):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME-minutes

#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(number_of_layers):
    """Define the preparation_time_in_minutes() function that takes the number_of_layers you want         
    to add to the lasagna as an argument and returns how many minutes you would spend making them. 
    Assume each layer takes 2 minutes to prepare."""
    return number_of_layers*PREPARATION_TIME


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Define the elapsed_time_in_minutes() function that takes two parameters as arguments:                 
    number_of_layers (the number of layers added to the lasagna) and elapsed_bake_time (the               
    number of minutes the lasagna has been baking in the oven). This function should return               
    the total number of minutes you have been cooking, or the sum of your preparation time                
    and the time the lasagna has already spent baking in the oven.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time


"""Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
