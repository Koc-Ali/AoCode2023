import os
import re

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
# filename = "2023_advent_input_A3_1.txt"
# filename = "2023_advent_input_A3_1.sample.txt"

filename = "2023_advent_input_A3_2.txt"
# filename = "2023_advent_input_A3_2.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
total_part_number = 0
total_numbers = 0
current_line = ''
previous_line = ''
upcoming_line = ''

def extract_numbers_with_position(line):
    result_numbers = []
    pattern = '\d+'
    numbers = re.finditer(pattern, line)

    # print all match object
    for number_obj in numbers:
        # print each re.Match object
        pos = number_obj.start()
        number = number_obj.group()
        result_numbers.append([number, pos])
    return(result_numbers)
def extract_asteriks_with_position(line):
    line = line.replace('.', '1')
    pattern = '[^0-9]'
    result_symbols = []
    adjacent_symbol ='*'

    symbols = re.finditer(pattern, line)
    # print all match object
    for symbol_obj in symbols:
        # print each re.Match object
        span = symbol_obj.start()
        symbol = symbol_obj.group()
        if symbol == adjacent_symbol:
            result_symbols.append([symbol, span])
    return(result_symbols)

def create_pos_list(number):
    pos_list = []
    num_length = len(number[0])
    pos_range = range(number[1]-1, number[1]+num_length+1)
    for pos in pos_range:
        pos_list.append(pos)
    return (pos_list)


def adjecent_numbers_in_a_line_for_asterik_overlapping(asterik, p_numbers, u_numbers):

    part_number_line = 0

    for p_number in p_numbers:
        p_range = create_pos_list(p_number)
        if asterik[1] in p_range:
           # check whether there is also a left number
           for u_number in u_numbers:
                u_range = create_pos_list(u_number)
                if asterik[1] in u_range:
                    adjacent_number_1 = p_number[0]
                    adjacent_number_2 = u_number[0]
                    adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                    print(adjacent_ratio, ', c = ', adjacent_number_1, ', u = ', adjacent_number_2, ' asterik = ', asterik)
                    # print(adjacent_ratio)
                    part_number_line += adjacent_ratio
    return (part_number_line)

def adjecent_numbers_in_a_line_for_asterik(asterik, c_numbers):
    # chef whether an asterik has a number as direct neigbour within same line
    adjacent_number_1 = 0
    adjacent_number_2 = 0

    for c_number in c_numbers:
        if asterik[1] == c_number[1] - 1: # asterik has a right number
            adjacent_number_1 = int(c_number[0])
        if asterik[1] == c_number[1] + len(c_number[0]): # asterik has a right number
            adjacent_number_2 = int(c_number[0])

    adjacent_ratio = adjacent_number_1 * adjacent_number_2
    if adjacent_ratio != 0:
        print(adjacent_ratio, ', same line = ', adjacent_number_1, ', u = ', adjacent_number_2, ' asterik = ', asterik)
    # print(adjacent_ratio)
    return (adjacent_ratio)


def adjecent_numbers_in_a_parallel_lines_for_asterik(asterik, c_numbers, p_numbers, u_numbers):
    part_number_line = 0
    # chef whether an asterik has a number as direct neigbour within same line

    for c_number in c_numbers:
        if asterik[1] == c_number[1] - 1: # asterik has a right number
           # check whether there is also a left number
            # previous line numbers
            for p_number in p_numbers:
                p_number_range = create_pos_list(p_number)
                if asterik[1] in p_number_range:
                    adjacent_number_1 = c_number[0]
                    adjacent_number_2 = p_number[0]
                    adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                    print(adjacent_ratio, ', c = ', adjacent_number_1, ', u = ', adjacent_number_2, ' asterik = ', asterik)
                    # print(adjacent_ratio)
                    part_number_line += adjacent_ratio
            # upcoming line numbers
            for u_number in u_numbers:
                u_number_range = create_pos_list(u_number)
                if asterik[1] in u_number_range:
                    adjacent_number_1 = c_number[0]
                    adjacent_number_2 = u_number[0]
                    adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                    print(adjacent_ratio, ', c = ', adjacent_number_1, ', u = ', adjacent_number_2, ' asterik = ', asterik)
                    # print(adjacent_ratio)
                    part_number_line += adjacent_ratio
        if asterik[1] == c_number[1]+len(c_number[0]): # asterik has a left number
            # previous line numbers
            for p_number in p_numbers:
                p_number_range = create_pos_list(p_number)
                if asterik[1] in p_number_range:
                    adjacent_number_1 = c_number[0]
                    adjacent_number_2 = p_number[0]
                    adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                    print(adjacent_ratio, ', c = ', adjacent_number_1, ', u = ', adjacent_number_2, ' asterik = ', asterik)
                    # print(adjacent_ratio)
                    part_number_line += adjacent_ratio
            # upcoming line numbers
            for u_number in u_numbers:
                u_number_range = create_pos_list(u_number)
                if asterik[1] in u_number_range:
                    adjacent_number_1 = c_number[0]
                    adjacent_number_2 = u_number[0]
                    adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                    print(adjacent_ratio, ', c = ', adjacent_number_1, ', u = ', adjacent_number_2, ' asterik = ', asterik)
                    # print(adjacent_ratio)
                    part_number_line += adjacent_ratio
    return (part_number_line)

def adjecent_numbers_in_a_diagol_for_asterik(asterik, p_numbers, u_numbers):
    part_number_line = 0
    # chef whether an asterik has a number as direct neigbour within same line

    for p_number in p_numbers:
        p_range = create_pos_list(p_number)
        if asterik[1] in p_range:
            # check whether there is also a left number
            for u_number in u_numbers:
                u_range = create_pos_list(u_number)
                if asterik[1] in u_range:
                    adjacent_number_1 = p_number[0]
                    adjacent_number_2 = u_number[0]
                    adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                    print(adjacent_ratio, ', c = ', adjacent_number_1, ', u = ', adjacent_number_2, ' asterik = ', asterik)
                    part_number_line += adjacent_ratio
    return (part_number_line)

for line in file:
    previous_line = current_line
    current_line = upcoming_line
    upcoming_line = line.strip()

    print(' ----- ')
    print('p line = ', previous_line)
    print('c line = ', current_line)
    print('u line = ', upcoming_line)

    # determine numbers with their string position for current line
    current_line_numbers = extract_numbers_with_position(current_line)
    previous_line_numbers = extract_numbers_with_position(previous_line)
    upcoming_line_numbers = extract_numbers_with_position(upcoming_line)

    # check whether current_line contains an asterics
    current_line_asteriks = extract_asteriks_with_position(current_line)
    part_number_current_line = 0

    for asterik in current_line_asteriks:

        # 1. check whether an asterik has two direkt neibhour numbers in same line
        print(' 1.check 2 in current line = ', part_number_current_line)
        part_number_current_line += adjecent_numbers_in_a_line_for_asterik(asterik, current_line_numbers)

        # 2. check whether an asterik has two direkt neibhour numbers in previous line
        print(' 2.check 2 in previous line = ', part_number_current_line)
        part_number_current_line += adjecent_numbers_in_a_line_for_asterik(asterik, previous_line_numbers)

        # 3. check whether an asterik has two direkt neibhour numbers in upcoming line
        print(' 3. check 2 in upcoming line = ', part_number_current_line)
        part_number_current_line += adjecent_numbers_in_a_line_for_asterik(asterik, upcoming_line_numbers)

        # 4. check whether an asterik has previous number overlapping position.
        print(' 4. check overlapping line = ', part_number_current_line)
        part_number_current_line += adjecent_numbers_in_a_line_for_asterik_overlapping(asterik, previous_line_numbers, upcoming_line_numbers)

        # 5. check whether an asterik in current line has direct neigbours with previous and upcoming numbers
        print(' 5. check previous, upcoming line = ', part_number_current_line)
        part_number_current_line += adjecent_numbers_in_a_parallel_lines_for_asterik(asterik, current_line_numbers, previous_line_numbers, upcoming_line_numbers)

    total_part_number += part_number_current_line

print('--- part number - final result = ', total_part_number)
