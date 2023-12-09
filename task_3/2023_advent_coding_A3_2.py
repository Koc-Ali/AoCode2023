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
part_number = 0
current_line = ''
previous_line = ''
upcoming_line = ''
current_line_numbers = []
current_line_symbols = []

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

def adjecent_numbers_in_a_line(line):
    part_number_line = 0
    # chef whether an asterik has a number as direct neigbour within same line

    current_line_asteriks = extract_asteriks_with_position(line)
    current_line_numbers = extract_numbers_with_position(line)

    for asterik in current_line_asteriks:
        adjacent_number_1 = 0
        adjacent_number_2 = 0
        for c_number in current_line_numbers:
            if asterik[1] == c_number[1] - 1: # asterik has a right number
               # check whether there is also a left number
                for cc_number in current_line_numbers:
                    if asterik[1] == cc_number[1] + len(cc_number): # asterik has a right number
                        adjacent_number_1 = c_number[0]
                        adjacent_number_2 = cc_number[0]
                        adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                        print('adjacent ration c+c =', adjacent_ratio, ', c = ', adjacent_number_1, ', u = ', adjacent_number_2)
                        part_number_line += adjacent_ratio
            if asterik[1] == c_number[1]+len(c_number[0]): # asterik has a left number
               # check whether there is also a left number
                for cc_number in current_line_numbers:
                    if asterik[1] == cc_number[1]-1: # asterik has a left number
                        adjacent_number_1 = c_number[0]
                        adjacent_number_2 = cc_number[0]
                        adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                        print('adjacent ration c+c =', adjacent_ratio, ', c = ', adjacent_number_1, ', u = ', adjacent_number_2)
                        part_number_line += adjacent_ratio
    return(part_number_line)

for line in file:
    previous_line = current_line
    current_line = upcoming_line
    upcoming_line = line.strip()

    # print(' ----- ')
    # print('p line = ', previous_line)
    # print('c line = ', current_line)
    # print('u line = ', upcoming_line)

    # determine numbers with their string position for current line
    current_line_numbers = extract_numbers_with_position(current_line)
    previous_line_numbers = extract_numbers_with_position(previous_line)
    upcoming_line_numbers = extract_numbers_with_position(upcoming_line)

    # check whether current_line contains an asterics
    current_line_asteriks = extract_asteriks_with_position(current_line)
#    print('current_line_asterics: ', current_line_asteriks)

    for asterik in current_line_asteriks:
        adjacent_number_1 = 0
        adjacent_number_2 = 0
        # check previous and upcoming lines
        for p_number in previous_line_numbers:
            if (asterik[1] >= p_number[1] - 1) and (asterik[1] <= p_number[1] + len(p_number[0])):
                adjacent_number_1 = p_number[0]
                # print('-- adjacent_number_1 p =', adjacent_number_1)
                for u_number in upcoming_line_numbers:
                    if (asterik[1] >= u_number[1] - 1) and (asterik[1] <= u_number[1] + len(u_number[0])):
                        adjacent_number_2 = u_number[0]
                        # print('-- adjacent_number_2 u =', adjacent_number_2)
        adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
        print('adjacent ration p+u =', adjacent_ratio, ', n1 = ', adjacent_number_1, ', n2 = ', adjacent_number_2)
        part_number += adjacent_ratio
    # chef whether an asterik has a number as direct neigbour with previous and upcoming line
    for asterik in current_line_asteriks:
        adjacent_number_1 = 0
        adjacent_number_2 = 0
        for c_number in current_line_numbers:
           if (asterik[1] == c_number[1] - 1) or (asterik[1] == c_number[1] + len(c_number[0])):
               adjacent_number_1 = c_number[0]
               # print('-- adjacent_number_1 c =', adjacent_number_1)
               # check whether previous OR upcoming number are adjacent
               for p_number in previous_line_numbers:
                   if (asterik[1] >= p_number[1] - 1) and (asterik[1] <= p_number[1] + len(p_number[0])):
                       adjacent_number_2 = p_number[0]
                       # print('-- adjacent_number_2 p =', adjacent_number_2)
                       adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                       # print('adjacent ration c+p =', adjacent_ratio)
                       print('adjacent ration c+p =', adjacent_ratio, ', c = ', adjacent_number_1, ', p = ', adjacent_number_2)
                       part_number += adjacent_ratio
               for u_number in upcoming_line_numbers:
                   if (asterik[1] >= u_number[1] - 1) and (asterik[1] <= u_number[1] + len(u_number[0])):
                       adjacent_number_2 = u_number[0]
                       # print('-- adjacent_number_2 u =', adjacent_number_2)
                       adjacent_ratio = int(adjacent_number_1) * int(adjacent_number_2)
                       print('adjacent ration c+u =', adjacent_ratio, ', c = ', adjacent_number_1, ', u = ', adjacent_number_2)
                       part_number += adjacent_ratio

    # chef whether an asterik has a number as direct neigbour within same line
    part_number += adjecent_numbers_in_a_line(current_line)

# last line was not processed so far
part_number += adjecent_numbers_in_a_line(upcoming_line)
# print final results
print('--- part number - final result = ', part_number)
