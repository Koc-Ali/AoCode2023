import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
# filename = "2023_advent_1.input.txt"
# filename = "2023_advent_1.input.sample.txt"

# filename = "2023_advent_1.input.sample.txt"
filename = "2023_advent_1.input.sample2.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
calibration_value = 0

# extract value out of line
def extract_first_digit(line):
    first_digit = 0
    # iterating over each character in the sting
    for index, char in enumerate(line):
        # chef if char is numeric
        if char.isdigit():
#            print('1. digit: ', char)
#            print('index of first number is: ', index)
            first_digit = char
            break
    return (first_digit, index)

def extract_digit_string (line):
    digit_as_string = ['one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine']
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
    return(first_digit)

for line in file:
    fields = line.strip()
    print(fields)

    first_digit, first_digit_index = extract_first_digit(fields)
    print('  first digit = ', first_digit, ', index = ', first_digit_index)

    if first_digit != 0:
        left_string_without_number = fields[:first_digit_index]
    else:
        left_string_without_number = fields
#    print(first_digit, ', index ', first_digit_index, ', left sting = ', left_string_without_number)

    # check if in left_string is string with number

    first_digit_string = extract_digit_string(left_string_without_number)
    print('  first left string digit = ', first_digit_string)

    if first_digit_string != -1:
        first_digit = first_digit_string
    print('  first left final digit = ', first_digit)




#    revirsed_string = fields[::-1]
#    last_digit = extract_first_digit(revirsed_string)

 #   current_value = int(first_digit)*10+ int(last_digit)
 #   print(current_value)

#    calibration_value += current_value
#    print(calibration_value)

# print final results
print(calibration_value)

