import os
import re

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
# filename = "2023_advent_input_A5_1.txt"
# filename = "2023_advent_input_A5_1.sample.txt"

filename = "2023_advent_input_A5_2.txt"
# filename = "2023_advent_input_A5_2.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution

lowest_location = 0
# mapping tables
seeds = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []

mapped_soils = []
mapped_fertilizers = []
mapped_waters = []
mapped_lights = []
mapped_temperatures = []
mapped_humidities = []
mapped_locations = []

def extract_seeds(line):
    seeds_numbers = re.findall('\d+', line)
    # print('seed number = ', seeds_numbers)
    seeds_ranges = []

    seeds_starting_values = seeds_numbers[::2]
    # consider pair of values. first is starting value. second range
    for index, seed in enumerate(seeds_numbers[::2]):
        # print(' index = ', index, ' seed = ', seed)
        start_value = int(seed)
        range_value = int(seeds_numbers[int(index*2)+1])
        end_value = start_value + range_value -1
        seeds_ranges.append([start_value, end_value])
        # print(' seed: ', seeds_ranges, ' start value = ', start_value, ' range = ', range_value)
    return (seeds_ranges)


def extract_mapping_lines(lines):
    mapping_lines = []
    for index, line in enumerate(lines):
        mapping_numbers = re.findall('\d+', line)
        #print('mapping umbers = ', mapping_numbers)
        mapping_lines.append(mapping_numbers)
    return (mapping_lines)


def is_destination_in_rev_mapping(destination, mapping):
    if (int(destination) >= int(mapping[0])) and (int(destination) < int(mapping[0]) + int(mapping[2])):
        return True
    else:
        return False

def is_seed_in_seed_list(seed_value, seeds):
    seed_in_list = False
    for seed in seeds:
        if (seed_value >= seed[0]) and (seed_value <= seed[1]):
            seed_in_list = True
    return seed_in_list

def calc_rev_source(destination, mapping_list):
    # destination is source, if no mapping conversion is required
    source = int(destination)
    mapping_possible = False

    # perform mapping conversion
    for mapping in mapping_list:
        if is_destination_in_rev_mapping(destination, mapping):
            source = int(destination) + int(mapping[1]) - int(mapping[0])
            mapping_possible = True
    # print(' rev source = ', source, ', destination =', destination)
    return mapping_possible, source


def calc_minimum_destination_value (humidity_to_location_map):
    minimum_value = 0
    for location in humidity_to_location_map:
        if minimum_value < int(location[0])+ int(location[2]):
            minimum_value = int(location[0])+ int(location[2])
    return minimum_value


lines = []

# read lines exclude empthy ones
for line in file:
    if len(line.split()) == 0:
        continue
    else:
        lines.append(line)

for index, line in enumerate(lines):
    if 'seeds' in line:
        seeds_start = index
    if 'seed-to-soil' in line:
        seed_to_soil_map_start = index
    if 'soil-to-fertilizer' in line:
        soil_to_fertilizer_map_start = index
    if 'fertilizer-to-water' in line:
        fertilizer_to_water_map_start = index
    if 'water-to-light' in line:
        water_to_light_map_start = index
    if 'light-to-temperature' in line:
        light_to_temperature_map_start = index
    if 'temperature-to-humidity' in line:
        temperature_to_humidity_map_start = index
    if 'humidity-to-location' in line:
        humidity_to_location_map_start = index

seeds = extract_seeds(lines[seeds_start])
print('input seeds = ', seeds)

seed_to_soil_map = extract_mapping_lines(lines[seed_to_soil_map_start + 1:soil_to_fertilizer_map_start])
print('input soils m = ', seed_to_soil_map)

soil_to_fertilizer_map = extract_mapping_lines(lines[soil_to_fertilizer_map_start + 1: fertilizer_to_water_map_start])
print('input fertilizer m = ', soil_to_fertilizer_map)

fertilizer_to_water_map = extract_mapping_lines(lines[fertilizer_to_water_map_start + 1: water_to_light_map_start])
print('input water m = ', fertilizer_to_water_map)

water_to_light_map = extract_mapping_lines(lines[water_to_light_map_start + 1: light_to_temperature_map_start])
print('input light m = ', water_to_light_map)

light_to_temperature_map = extract_mapping_lines(lines[light_to_temperature_map_start + 1: temperature_to_humidity_map_start])
print('input temperature m = ', light_to_temperature_map)

temperature_to_humidity_map = extract_mapping_lines(lines[temperature_to_humidity_map_start + 1: humidity_to_location_map_start])
print('input humidity m = ', temperature_to_humidity_map)

humidity_to_location_map = extract_mapping_lines(lines[humidity_to_location_map_start + 1: len(lines)])
print('input location m = ', humidity_to_location_map)

# reverse mapping

# calc minimum destination range
max_destination_mapping_number = calc_minimum_destination_value (humidity_to_location_map)
print(' maximum mapping number = ', max_destination_mapping_number)
for destination_index in range (0, max_destination_mapping_number):

    # print('--- destination value = ', destination_index)

    mapped, humidity_value = calc_rev_source(destination_index, humidity_to_location_map)
    #print('mapped =', mapped, 'rev humidity: ', humidity_value)

    mapped, temperature_value = calc_rev_source(humidity_value, temperature_to_humidity_map)
    # print('mapped =', mapped, 'rev temperature: ', temperature_value)

    mapped, lights_value = calc_rev_source(temperature_value, light_to_temperature_map)
    # print('mapped =', mapped, 'rev lights: ', lights_value)

    mapped, water_value = calc_rev_source(lights_value, water_to_light_map)
    # print('mapped =', mapped, 'rev water: ', water_value)

    mapped, fertilizer_value = calc_rev_source(water_value, fertilizer_to_water_map)
    # print('mapped =', mapped, 'rev fertilizer: ', fertilizer_value)

    mapped, soil_value = calc_rev_source(fertilizer_value, soil_to_fertilizer_map)
    # print('mapped =', mapped, 'rev soil: ', soil_value)

    mapped, seed_value = calc_rev_source(soil_value, seed_to_soil_map)
    # print('mapped =', mapped, 'soil number = ', soil_value, ' ==> ', ' rev seed: ', seed_value)

    seed_value_in_seed_list = is_seed_in_seed_list(seed_value, seeds)
    # print(' is calc seed in seeds = ', seed_value_in_seed_list)
    if seed_value_in_seed_list:
        lowest_location = destination_index
        break

# print final results
print(' -- final result = ', lowest_location)


