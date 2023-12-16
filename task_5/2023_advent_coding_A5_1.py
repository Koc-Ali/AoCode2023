import os
import re

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
# filename = "2023_advent_input_A5_1.txt"
filename = "2023_advent_input_A5_1.sample.txt"

# filename = "2023_advent_input_A5_2.txt"
# filename = "2023_advent_input_A5_2.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
lowest_location = 0
seeds = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []

def read_seeds():

def extract_seed_to_soil_map():
def extract_soil_to_fertilizer_map():
def extract_fertilizer_to_water_map():
def extract_water_to_light_map():
def extract_light_to_temperature_map():
def extract_temperature_to_humidity_map():
def extract_humidity_to_location_map():

def extract_numbers(card_line):
    result_numbers = []
    pattern = '\d+'

    # find and delete pre-amble
    pos_card_info = card_line.find(':')
    pos_card_splitter = card_line.find('|')
    winning_string = card_line[pos_card_info:pos_card_splitter]
    own_string = card_line[pos_card_splitter:]

    winning_numbers = re.findall(pattern, winning_string)
    own_numbers = re.findall(pattern, own_string)

    return winning_numbers, own_numbers

for line in file:
    # read input file
    almanac_line = line.strip()

    print(almanac_line)
    # check section
    if line ==


    winning_numbers, own_numbers = extract_numbers(card_line)
    print(winning_numbers)
    print(own_numbers)

    # calc points for all card
    card_matches = 0
    card_match_points = 0
    for index, winning_numb in enumerate(winning_numbers):
        # calc points for EACH card
        if winning_numb in own_numbers:
            card_matches += 1
            if card_matches == 1:
                card_match_points = 1
            else:
                card_match_points *= 2
    total_worth_points += card_match_points
    print('card match counted = ', card_matches)
    print('card match points = ', card_match_points)
    print('card total match points = ', total_worth_points)

# print final results
print(' -- final result = ', total_worth_points)
