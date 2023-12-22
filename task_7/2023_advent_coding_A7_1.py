import os
import re


# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2023_advent_input_A7_1.txt"
# filename = "2023_advent_input_A7_1.sample.txt"

# filename = "2023_advent_input_A7_2.txt"
# filename = "2023_advent_input_A7_2.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
total_winnings = 0
lines = []
hands = []

card_strengths_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1']

# const for strength
Five_of_a_kind = '5K'
Four_of_a_kind = '4K'
Full_house = 'FH'
Three_of_a_kind = '3K'
Two_Pairs = '2P'
One_Pair = '1P'
High_Card = 'HC'


def extract_hands (line):
    hands = line[1].strip().split()
    hands.append('0') # add strength
    # print('hands = ', hands)
    return (hands)

def calc_hands_strengths(hands):
    for hand in hands:
        max_accurances = count_max_occurances(hand[0])
        strength = max(max_accurances)

        # chef for five and four of a kind
        if strength == [5]:
            # print(' - 5 of kind = ', strength, ' hand = ', hand)
            hand[2] = Five_of_a_kind
        if strength == [4]:
            # print(' - 4 of kind = ', strength, ' hand = ', hand)
            hand[2] = Four_of_a_kind
        if strength == [3]: # check for fullhouse and tree of a kind
            count_2 = max_accurances.count([2])
            if count_2 == 1:
                # print(' - full house = ', strength, ' hand = ', hand)
                hand[2] = Full_house
            else:
                # print(' - 3 of kind = ', strength, ' hand = ', hand)
                hand[2] = Three_of_a_kind
        if strength == [2]: # check for two pairs or one pair
            count_2 = max_accurances.count([2])
            if count_2 == 2:
                # print(' - Two pair = ', strength, ' hand = ', hand)
                hand[2] = Two_Pairs
            else:
                # print(' - One pair = ', strength, ' hand = ', hand)
                hand[2] = One_Pair
        if strength == [1]:
            # print(' - high card = ', strength, ' hand = ', hand)
            hand[2] = High_Card
    return hands

def sort_and_calc_hands(hands):
    # find all five of a kind hands
    five_of_ak = filter_hands(hands, Five_of_a_kind)
    print(five_of_ak)

    four_of_ak = filter_hands(hands, Four_of_a_kind)
    print(four_of_ak)

    full_h = filter_hands(hands, Full_house)
    print(full_h)

    three_of_ak = filter_hands(hands, Three_of_a_kind)
    print(three_of_ak)

    two_p = filter_hands(hands, Two_Pairs)
    print(two_p)

    one_p = filter_hands(hands, One_Pair)
    print(one_p)

    high_k = filter_hands(hands, High_Card)
    print(high_k)

    # soft each list
    five_of_ak = quicksort(five_of_ak)
    # five_of_ak.sort(reverse=True, key=lambda hand: hand[0])
    print(' sorted list: ', five_of_ak)

    # four_of_ak.sort(reverse=True, key=lambda hand: hand[0])
    four_of_ak = quicksort(four_of_ak)
    print(' sorted list: ', four_of_ak)

    # full_h.sort(reverse=True, key=lambda hand: hand[0])
    full_h = quicksort(full_h)
    print(' sorted list: ', full_h)

    # three_of_ak.sort(reverse=True, key=lambda hand: hand[0])
    three_of_ak = quicksort(three_of_ak)
    print(' sorted list: ', three_of_ak)

    # two_p.sort(reverse=True, key=lambda hand: hand[0])
    two_p = quicksort(two_p)
    print(' sorted list: ', two_p)

    # one_p.sort(reverse=True, key=lambda hand: hand[0])
    one_p = quicksort(one_p)
    print(' sorted list: ', one_p)

    # high_k.sort(reverse=True, key=lambda hand: hand[0])
    high_k = quicksort(high_k)
    print(' sorted list: ', high_k)

    # calc high_k winnings
    ranking_start = 1

    win_high_k, ranking_start = calc_hands_winning(ranking_start, high_k)
    print(' winning = ', win_high_k)

    win_one_p, ranking_start = calc_hands_winning(ranking_start, one_p)
    print(' winning = ', win_one_p)

    win_two_p, ranking_start = calc_hands_winning(ranking_start, two_p)
    print(' winning = ', win_two_p)

    win_three_of_ak, ranking_start = calc_hands_winning(ranking_start, three_of_ak)
    print(' winning = ', win_three_of_ak)

    win_full_h, ranking_start = calc_hands_winning(ranking_start, full_h)
    print(' winning = ', win_full_h)

    win_four_of_ak, ranking_start = calc_hands_winning(ranking_start, four_of_ak)
    print(' winning = ', win_four_of_ak)

    win_five_of_ak, ranking_start = calc_hands_winning(ranking_start, five_of_ak)
    print(' winning = ', win_five_of_ak)

    total_win = win_five_of_ak + win_four_of_ak + win_full_h + win_three_of_ak + win_two_p + win_one_p + win_high_k
    print(' total win = ', total_win)
    return total_win

def calc_hands_winning(ranking_start, sub_list):
    total_winning_sub_list = 0
    ranking = ranking_start
    for hand in sub_list:
        total_winning_sub_list += ranking * int(hand[1])
        # print(' --- ranking = ', ranking, ', value = ', int(hand[1]))
        ranking += 1
    return total_winning_sub_list, ranking


def filter_hands(hands, filter):
    filtered_elements = []
    for element in hands:
        if element[2] == filter:
            filtered_elements.append(element)
    return filtered_elements
def count_max_occurances(text):
    max_counters = []

    unique_chars = list(set(text))
    for index, text_ch in enumerate(unique_chars):
        counter = text.count(text_ch)
        max_counters.append([counter])
    return max_counters


def quicksort(hands):
    if len(hands) <= 1:
        return hands
    else:
        pivot = hands[0]
        left = [x for x in hands[1:] if quicksort_pivot_greater(x, pivot) == True]
        right = [x for x in hands[1:] if quicksort_pivot_greater(x, pivot) == False]
        hands_sorted = quicksort(left) + [pivot] + quicksort(right)
        return hands_sorted

def quicksort_pivot_greater (x, pivot):

    for index, card in enumerate(pivot[0]):
        order_pivot = card_strengths_order.index(pivot[0][index])
        # print(' order pivot = ', order_pivot)
        order_x = card_strengths_order.index(x[0][index])
        # print(' order x = ', order_x)
        if order_pivot < order_x:
            return True
        if order_pivot > order_x:
            return False
    return False

# read lines exclude empthy ones
for line in file:
    if len(line.split()) == 0:
        continue
    else:
        lines.append(line)

for line in enumerate(lines):
    next_hand = extract_hands(line)
    hands.append(next_hand)

hands = calc_hands_strengths(hands)
print(' hands input = ', hands)

total_winnings = sort_and_calc_hands(hands)

# print final results
print(' -- final result = ', total_winnings)

