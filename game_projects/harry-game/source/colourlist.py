# dictionary of colours and associated RGB values

"""Colourlist is a module containing a dictionary of colours and their RGB values.
It also contains a function to print all the colours in the dictionary."""

colours = {}  # declare a color dictionary
colours['yellow'] = [1.0, 1.0, 0.0]  # fill each entry of the color dictionary with a list of three floats
colours['blue'] = [0.0, 0.0, 1.0]
colours['red'] = [1.0, 0.0, 0.0]
colours['green'] = [0.0, 1.0, 0.0]
colours['sienna'] = [0.627, 0.322, 0.176]
colours['hotpink'] = [1.0, 0.412, 0.706]

def print_available_colours(colours):
    for shade in list(colours):
        print(shade)

if __name__ == "__main__":
    # only run this code if colors.py is run as the top-level function
    # ignore if colors.py is imported as a module
    print('executing colors.py as the main routine')
    print('we have definitions of:')
    print_available_colours(colours)