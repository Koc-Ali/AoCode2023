import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
# filename = "2023_advent_1.input.txt"
filename = "2023_advent_1.input2.txt"
# filename = "2023_advent_1.input.sample.txt"

# filename = "2023_advent_1.input.sample.txt"
# filename = "2023_advent_1.input.sample2.txt"


path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
calibration_value = 0
digit_as_string = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# extract value out of line
def extract_first_digit(line):
    first_digit = 0
    # iterating over each character in the sting
    for index, char in enumerate(line):
        # chef if char is numeric
        if char.isdigit():
            first_digit = char
            break
    return (first_digit, index)

def extract_first_digit_string (line):
    first_found_position = -1
    first_digit = -1
    first_digit_string =''

    for digit_string in digit_as_string:
        found_position = line.find(digit_string)
        if found_position != -1:
#            print('a) found_number_string = ', digit_string, ', found pos =', found_position, ', first found pos =', first_found_position)
            if first_found_position == -1:
                first_found_position = found_position
                first_digit_string = digit_string
            elif found_position < first_found_position:
                first_found_position = found_position
                first_digit_string = digit_string
#            print('b) first digit string = ', first_digit_string, ', first found pos =', first_found_position)

    if first_digit_string != '':
        first_digit = digit_as_string.index(first_digit_string)+1
    return (first_digit)

def extract_last_digit_string (line):
    last_found_position = -1
    last_digit = -1
    last_digit_string =''

    for digit_string in digit_as_string:
        found_position = line.rfind(digit_string) # search revised!
        if found_position != -1:
            # print('a) found_number_string = ', digit_string, ', found pos =', found_position, ', last found pos =', last_found_position)
            if last_found_position == -1:
                last_found_position = found_position
                last_digit_string = digit_string
            elif found_position > last_found_position:
                last_found_position = found_position
                last_digit_string = digit_string
            # print('b) last digit string = ', last_digit_string, ', last found pos =', last_found_position)

    if last_digit_string != '':
        last_digit = digit_as_string.index(last_digit_string)+1
    return (last_digit)

for line in file:
    fields = line.strip()
    # print(fields)

    first_digit, first_digit_index = extract_first_digit(fields)
    # print('  first digit = ', first_digit, ', index = ', first_digit_index)

    if first_digit != 0:
        left_string_without_number = fields[:first_digit_index]
    else:
        left_string_without_number = fields

    # check if in left_string is string with number
    first_digit_string = extract_first_digit_string(left_string_without_number)
    # print('  first left string digit = ', first_digit_string)

    if first_digit_string != -1:
        first_digit = first_digit_string
    # print('  first left final digit = ', first_digit)

    # find last digit and position in string
    revised_string = fields[::-1]
    last_digit, last_digit_position = extract_first_digit(revised_string)
    last_digit_position = len(fields)-last_digit_position-1
    # print('  - last digit =', last_digit, ', last digit pos =', last_digit_position)

    # cut string from last digit to the end of string
    if last_digit != 0:
        right_string_without_digit = fields[last_digit_position+1:]
    else:
        right_string_without_digit = fields[last_digit_position:]
    # print('   - rigth string without digit =', right_string_without_digit)

    # check remaining string regarding digit string
    last_digit_string = extract_last_digit_string(right_string_without_digit)
    # print('  last left string digit = ', last_digit_string)

    if last_digit_string != -1:
        last_digit = last_digit_string
    # print('  last left final digit = ', last_digit)

    current_value = int(first_digit)*10 + int(last_digit)
    calibration_value += current_value
    print(fields)
    print(current_value)
    #print(calibration_value)


# print final results
print('-- final calibration value = ', calibration_value)

