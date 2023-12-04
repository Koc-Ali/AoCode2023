import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2023_advent_1.input.txt"
# filename = "2023_advent_1.input.sample.txt"

# filename = "2023_advent_1.input.sample.txt"
# filename = "2023_advent_1.input.sample2.txt"

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
    return (first_digit)

for line in file:
    fields = line.strip()
#    print(fields)

    first_digit = extract_first_digit(fields)

    revirsed_string = fields[::-1]
    last_digit = extract_first_digit(revirsed_string)

    current_value = int(first_digit)*10+ int(last_digit)
    print(current_value)

    calibration_value += current_value
    print(calibration_value)

# print final results
print(calibration_value)
