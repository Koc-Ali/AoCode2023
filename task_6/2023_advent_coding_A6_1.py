import os
import re

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2023_advent_input_A6_1.txt"
# filename = "2023_advent_input_A6_1.sample.txt"

# filename = "2023_advent_input_A6_2.txt"
# filename = "2023_advent_input_A6_2.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
ways_to_beat_number = 1
lines = []
times = []
distances = []

def extract_times(line):
    time_values = re.findall('\d+', line)
    print('time numbers = ', time_values)
    return (time_values)

def extract_distances(line):
    distance_values = re.findall('\d+', line)
    print('distance numbers = ', distance_values)
    return (distance_values)

def calc_distances (time, record_destination):
    beating_ways = []
    beating_ways_amount = 0

    time_range = range (0, int(time))
    for speed in time_range:
        distance = (int(time)-int(speed)) * int(speed)
        if distance > int(record_destination):
            beating_ways.append([distance])
            beating_ways_amount += 1
        else:
            beating_ways.append([-1])
    return (beating_ways_amount, beating_ways)


# read lines exclude empthy ones
for line in file:
    if len(line.split()) == 0:
        continue
    else:
        lines.append(line)

for index, line in enumerate(lines):
    if 'Time' in line:
        times = extract_times(line)
    if 'Distance' in line:
        distances = extract_distances(line)

for index, race in enumerate(times):
    winning_races, beeting_ways = calc_distances(race, distances[index])
    print(' race = ', index, ' , winning races = ', winning_races)
    ways_to_beat_number *= winning_races

# print final results
print(' -- final result = ', ways_to_beat_number)
