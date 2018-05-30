from random import randint

dic = {}

dic['hot pink'] = [1.00, 0.43, 0.78] # fill each entry of the color dictionary with a list of three floats
dic['blue'] = [0.0, 0.0, 1.0]
dic['white'] = [1.0, 1.0, 1.0]
dic['yellow'] = [1.0, 1.0, 0.0]
dic['red'] = [1.0, 0.0, 0.0]
dic['green'] = [0.0, 1.0, 0.0]
dic['sienna'] = [0.627, 0.322, 0.176]

def random_colour():
    """
    From the dictrionary of colours
    :return: a random colour RGB code as a list
    """

    colour = list(dic.values())[randint(0, len(dic) - 1)]
    return colour

def availableColors():
    """
    :return: a list of all the avaible colours in the dictionary
    """

    return list(dic.keys())

if __name__ == '__main__':
    print(availableColors())