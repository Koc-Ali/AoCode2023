import os
import re

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2023_advent_input_A4_1.txt"
# filename = "2023_advent_input_A4_1.sample.txt"

# filename = "2023_advent_input_A4_2.txt"
# filename = "2023_advent_input_A4_2.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
total_worth_points = 0
card_winning_numbers = []
card_own_numbers = []

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
    # read all cards extract numbers
    card_line = line.strip()

    print(card_line)
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
