import os
import re

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
# filename = "2023_advent_input_A4_1.txt"
# filename = "2023_advent_input_A4_1.sample.txt"

filename = "2023_advent_input_A4_2.txt"
# filename = "2023_advent_input_A4_2.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
total_scratchcards = 0
cards = []
card_winning_numbers = []
card_own_numbers = []
total_worth_points = 0
max_read_cards = 0

def extract_numbers(card_line):
    result_numbers = []
    pattern = '\d+'

    # find and delete pre-amble
    pos_card_info = card_line.find(':')
    pos_card_splitter = card_line.find('|')
    winning_string = card_line[pos_card_info:pos_card_splitter]
    own_string = card_line[pos_card_splitter:]
    card_number_string = card_line[:pos_card_info]
    card_numbers = re.findall(pattern, card_number_string)
    card_number = int(card_numbers[0])
    winning_numbers = re.findall(pattern, winning_string)
    own_numbers = re.findall(pattern, own_string)

    return card_number, winning_numbers, own_numbers

def calc_matching_point(win_numbers, own_numbers):
    # calc points for all card
    card_matches = 0
    card_match_points = 0
    for index, winning_numb in enumerate(win_numbers):
        # calc points for EACH card
        if winning_numb in own_numbers:
            card_matches += 1
            if card_matches == 1:
                card_match_points = 1
            else:
                card_match_points *= 2
    return card_matches, card_match_points

def extend_cards_according_match_points(match_card):
    # print('match_card = ', match_card)
    required_copies = match_card[1]
    # print(' required copies = ', required_copies)
    # check whole cards
    for ccard in cards:
        # if it matches to match_card, add required cards
        if ccard[0] == match_card[0]:
            for index in range(required_copies):
                # get card to be copied
                card_to_be_copied = cards[int(match_card[0])+index]
                # print(' card to be copied = ', card_to_be_copied)
                cards.append(card_to_be_copied)
                # print(' new cards list = ', cards)

for line in file:
    # read all cards extract numbers
    card_line = line.strip()
    max_read_cards += 1

    # print(card_line)
    card_number, winning_numbers, own_numbers = extract_numbers(card_line)
    # print(winning_numbers)
    # print(own_numbers)

    card_matches, card_match_points = calc_matching_point(winning_numbers, own_numbers)

    total_worth_points += card_match_points

    cards.append([card_number, card_matches])

    # print('card match counted = ', card_matches)
    # print('card match points = ', card_match_points)
    # print('card total match points = ', total_worth_points)
    # print('card match points = ', cards)


# iterate all orginal card sets and add cards according to cards match points
for card in cards[:max_read_cards]:
    extend_cards_according_match_points(card)
    #print(card)
    #print(cards)

# print final results
# print(' -- final result cards = ', cards)
print(' -- final result cards amount = ', len(cards))

