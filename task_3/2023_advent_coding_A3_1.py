import os
import re

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2023_advent_input_A3_1.txt"
# filename = "2023_advent_input_A3_1.sample.txt"

# filename = "2023_advent_input_A3_2.txt"
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
def extract_symbols_with_position(line):
    line = line.replace('.', '1')
    pattern = '[^0-9]'
    result_symbols = []

    symbols = re.finditer(pattern, line)
    # print all match object
    for symbol_obj in symbols:
        # print each re.Match object
        span = symbol_obj.start()
        symbol = symbol_obj.group()
        result_symbols.append([symbol, span])
    return(result_symbols)

for line in file:
    previous_line = current_line
    current_line = upcoming_line
    upcoming_line = line.strip()

    print(' ----- ')
    print('previous line = ', previous_line)
    print('current line = ', current_line)
    print('upcoming line = ', upcoming_line)

    # determine numbers with their string position for current line
    current_line_numbers = extract_numbers_with_position(current_line)
    print('current_line_numbers: ', current_line_numbers)

    # extract symbols with their sting position  for current line
    current_line_symbols = extract_symbols_with_position(current_line)
    print('current_line_symbols: ', current_line_symbols)

    # check whether current line symbols are neighbors of numbers in current line
    # for number in current_line_numbers:
    for c_number in current_line_numbers:
        for c_symbol in current_line_symbols:
            if (c_symbol[1] == c_number[1]-1) or (c_symbol[1] == c_number[1] + len(c_number[0])):
                # valid value
                print('-- current line symbol check - valid value ---' , c_number)
                part_number += int(c_number[0])

    # check whether previous line symbols are neighbors of numbers in current line
    previous_line_symbols = extract_symbols_with_position(previous_line)
    print('- previous line symbols tbc: ', previous_line_symbols)
    for c_number in current_line_numbers:
        for p_symbol in previous_line_symbols:
            if (p_symbol[1] >= c_number[1]-1) and (p_symbol[1] <= c_number[1] + len(c_number[0])):
                # valid value
                print('-- previous line symbol check - valid value ---' , c_number)
                part_number += int(c_number[0])

    # check whether previous line symbols are neighbors of numbers in current line
    upcoming_line_symbols = extract_symbols_with_position(upcoming_line)
    print('- upcoming line symbols tbc: ', upcoming_line_symbols)
    for c_number in current_line_numbers:
        for u_symbol in upcoming_line_symbols:
            if (u_symbol[1] >= c_number[1]-1) and (u_symbol[1] <= c_number[1] + len(c_number[0])):
                # valid value
                print('-- upcoming line symbol check - valid value ---' , c_number)
                part_number += int(c_number[0])


# last line was not processed so far

# determine numbers with their string position for current line
last_line_numbers = extract_numbers_with_position(upcoming_line)
print('last_line_numbers: ', last_line_numbers)

# extract symbols with their sting position  for current line
last_line_symbols = extract_symbols_with_position(upcoming_line)
print('last_line_symbols: ', last_line_symbols)

# check whether last line symbols are neighbors of numbers in last line
# for number in last_line_numbers:
for l_number in last_line_numbers:
    for l_symbol in last_line_symbols:
        if (l_symbol[1] == l_number[1]-1) or (l_symbol[1] == l_number[1] + len(l_number[0])):
            # valid value
            print('-- valid value ---' , l_number)
            part_number += int(l_number[0])

# check whether previous line symbols are neighbors of numbers in last line
current_line_symbols = extract_symbols_with_position(current_line)
for l_number in last_line_numbers:
    for c_symbol in current_line_symbols:
        if (c_symbol[1] >= l_number[1]-1) and (c_symbol[1] <= l_number[1] + len(l_number[0])):
            # valid value
            print('-- valid value ---' , l_number)
            part_number += int(l_number[0])

# print final results
print('--- part number - final result = ', part_number)
