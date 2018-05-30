"""Colors is a list of colors the game_function can take"""

color = {}  # declare a color dictionary
color['yellow'] = [1.0, 1.0, 0.0]  # fill each entry of the color dictionary with a list of three floats
color['red'] = [1.0, 0.0, 0.0]
color['green'] = [0.0, 1.0, 0.0]


def printAvailableColors():
    """Function prints available colors"""
    print('\tyellow')
    print('\tred')
    print('\tgreen')
