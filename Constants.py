# constants

import enum

''' 
The order of political parties in Constants.PARTIES tuple is predefined and cannot be changed
Constants.PARTIES[0] = 'PiS'
Constants.PARTIES[1] = 'KO'
Constants.PARTIES[2] = 'SLD'
Constants.PARTIES[3] = 'PSL'
Constants.PARTIES[4] = 'Konf'
Constants.PARTIES[5] = 'BS'
Constants.PARTIES[6] = 'MN'
'''
PARTIES = ('PiS', 'KO', 'SLD', 'PSL', 'Konf', 'BS', 'MN')
NUMBER_OF_PARTIES = 7
NUMBER_OF_QUOTINETS = 15

ELECTION_THRESHOLD = 5.0

CONSTITUENCY_NAMES = [
    'Legnica', 'Wałbrzych', 'Wrocław', 'Bydgoszcz', 'Toruń',
    'Lublin', 'Chełm', 'Zielona Góra', 'Łódź', 'P. Trybunalski',
    'Sieradz', 'Chrzanów', 'Kraków', 'Nowy Sącz', 'Tarnów',
    'Płock', 'Radom', 'Siedlce', 'Warszawa miasto', 'Warszawa powiat',
    'Opole', 'Krosno', 'Rzeszów', 'Białystok', 'Gdańsk',
    'Gdynia', 'Bielsko-Biała', 'Częstochowa', 'Gliwice', 'Rybnik',
    'Katowice', 'Sosnowiec', 'Kielce', 'Elbląg', 'Olsztyn',
    'Kalisz', 'Konin', 'Piła', 'Poznań', 'Koszalin',
    'Szczecin'
]

# number of inhabitants with right to vote
INHABITANTS = [
    787416, 539545, 988061, 804077, 832502,
    959177, 771648, 800699, 642203, 586015,
    786549, 514765, 938869, 614295, 579603,
    671219, 574038, 763101, 1561289, 832675,
    808931, 710602, 988577, 947710, 830798,
    936485, 612348, 486784, 611771, 574191,
    777770, 564891, 1031221, 503061, 636139,
    797144, 617224, 610758, 692746, 515403,
    826850
]

SEATS = [
    12, 8, 14, 12, 13,
    15, 12, 12, 10, 9,
    12, 8, 14, 10, 9,
    10, 9, 12, 20, 12,
    12, 11, 15, 14, 12,
    14, 9, 7, 9, 9,
    12, 9, 16, 8, 10,
    12, 9, 9, 10, 8,
    12
]

# based on the results of the parliamentary elections in 2015
TURNOUT = [
    46.71, 44.83, 54.08, 47.87, 44.90,
    52.01, 45.3, 44.63, 56.74, 50.26,
    48.47, 54.46, 58.81, 52.18, 51.85,
    46.22, 49.38, 50.56, 70.80, 60,
    43.12, 47.47, 52.56, 57.1, 52.55,
    51.28, 56.35, 49.83, 49.12, 51.82,
    53.92, 51.41, 46.82, 41.3, 43.13,
    47.27, 46.64, 46.07, 60.23, 43.63,
    47.27
]

class Biases(enum.Enum):
    LARGE_CITY_W = 1
    LARGE_CITY_E = 2
    MEDIUM_CITY_W = 3
    MEDIUM_CITY_E = 4
    SMALL_CITY_W = 5
    SMALL_CITY_E = 6

CONSTITUENCY_BIASES = [
    Biases.SMALL_CITY_W, Biases.MEDIUM_CITY_W, Biases.LARGE_CITY_W, Biases.MEDIUM_CITY_W, Biases.MEDIUM_CITY_E,
    Biases.LARGE_CITY_E, Biases.SMALL_CITY_E, Biases.MEDIUM_CITY_W, Biases.LARGE_CITY_W, Biases.MEDIUM_CITY_E,
    Biases.MEDIUM_CITY_E, Biases.MEDIUM_CITY_E, Biases.LARGE_CITY_E,  Biases.SMALL_CITY_E, Biases.MEDIUM_CITY_E,
    Biases.MEDIUM_CITY_E, Biases.MEDIUM_CITY_E, Biases.SMALL_CITY_E, Biases.LARGE_CITY_W, Biases.LARGE_CITY_E,
    Biases.LARGE_CITY_W, Biases.SMALL_CITY_E, Biases.SMALL_CITY_E, Biases.MEDIUM_CITY_E, Biases.LARGE_CITY_W,
    Biases.LARGE_CITY_W, Biases.LARGE_CITY_E, Biases.MEDIUM_CITY_W, Biases.MEDIUM_CITY_W, Biases.MEDIUM_CITY_E,
    Biases.LARGE_CITY_W, Biases.MEDIUM_CITY_W, Biases.MEDIUM_CITY_E, Biases.MEDIUM_CITY_W, Biases.MEDIUM_CITY_W,
    Biases.SMALL_CITY_W, Biases.MEDIUM_CITY_E, Biases.MEDIUM_CITY_W, Biases.LARGE_CITY_W, Biases.MEDIUM_CITY_W,
    Biases.MEDIUM_CITY_W,
]
''' 
CONSTITUENCY_FEATURES uses the bits in CONSTITUENCY_FEATURES WORD to set distinct features of a constituency

CONSTITUENCY_FEATURE:
    | likes_MN || likes_KONF || likes_KP || likes_SLD || likes_KO || likes_PiS |                         
    |    32    ||     16     ||     8    ||     4     ||     2    ||     1     |

example: 
CONSTITUENCY_FEATURE[ i-th constutuency ] = 25 [dec] or 00011001 [bin]
likes_PiS  = True
likes_KP   = True
likes_KONF = True
'''

CONSTITUENCY_FEATURES = [
    4, 2, 8, 4, 4,
    9, 25, 4, 6, 9,
    8, 1, 16, 17, 25,
    8, 9, 9, 24, 16,
    32, 9, 9, 13, 18,
    2, 0, 12, 18, 0,
    14, 6, 9, 10, 30,
    8, 20, 20, 12, 10,
    18
]

NUMBER_OF_CONSTITUENCIES = 41