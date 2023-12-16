import os
import re

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2023_advent_input_A5_1.txt"
# filename = "2023_advent_input_A5_1.sample.txt"

# filename = "2023_advent_input_A5_2.txt"
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
    return (seeds_numbers)


def extract_mapping_lines(lines):
    mapping_lines = []
    for index, line in enumerate(lines):
        mapping_numbers = re.findall('\d+', line)
        # print('mapping umbers = ', mapping_numbers)
        mapping_lines.append(mapping_numbers)
    return (mapping_lines)


def is_source_in_mapping(source, mapping):
    if (int(source) >= int(mapping[1])) and (int(source) < int(mapping[1]) + int(mapping[2])):
        return True
    else:
        return False


def calc_destination(source, mapping_list):
    # destination is source, if no mapping conversion is required
    destination = int(source)

    # perform mapping conversion
    for mapping in mapping_list:
        if is_source_in_mapping(source, mapping):
            destination = int(source) - int(mapping[1]) + int(mapping[0])
    return destination

def calc_destination_list(source_list, mapping_list):
    mapped_list = []
    for source in source_list:
        mapped_value = calc_destination(source, mapping_list)
        mapped_list.append(mapped_value)
    return (mapped_list)

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
print(seeds)

seed_to_soil_map = extract_mapping_lines(lines[seed_to_soil_map_start + 1:soil_to_fertilizer_map_start])
print(seed_to_soil_map)

soil_to_fertilizer_map = extract_mapping_lines(lines[soil_to_fertilizer_map_start + 1: fertilizer_to_water_map_start])
print(soil_to_fertilizer_map)

fertilizer_to_water_map = extract_mapping_lines(lines[fertilizer_to_water_map_start + 1: water_to_light_map_start])
print(fertilizer_to_water_map)

water_to_light_map = extract_mapping_lines(lines[water_to_light_map_start + 1: light_to_temperature_map_start])
print(water_to_light_map)

light_to_temperature_map = extract_mapping_lines(
    lines[light_to_temperature_map_start + 1: temperature_to_humidity_map_start])
print(light_to_temperature_map)

temperature_to_humidity_map = extract_mapping_lines(
    lines[temperature_to_humidity_map_start + 1: humidity_to_location_map_start])
print(temperature_to_humidity_map)

humidity_to_location_map = extract_mapping_lines(lines[humidity_to_location_map_start + 1: len(lines)])
print(humidity_to_location_map)

# mapping

mapped_soils = calc_destination_list(seeds, seed_to_soil_map)
print('mapped souls: ', mapped_soils)

mapped_fertilizers = calc_destination_list(mapped_soils, soil_to_fertilizer_map)
print('mapped fertilizers: ', mapped_fertilizers)

mapped_waters = calc_destination_list(mapped_fertilizers, fertilizer_to_water_map)
print('mapped waters: ', mapped_waters)

mapped_lights = calc_destination_list(mapped_waters, water_to_light_map)
print('mapped lights: ', mapped_lights)

mapped_temperatures = calc_destination_list(mapped_lights, light_to_temperature_map)
print('mapped temperatures: ', mapped_temperatures)

mapped_humidities = calc_destination_list(mapped_temperatures, temperature_to_humidity_map)
print('mapped humudities: ', mapped_humidities)

mapped_locations = calc_destination_list(mapped_humidities, humidity_to_location_map)
print('mapped locations: ', mapped_locations)

lowest_location = min(mapped_locations)

# print final results
print(' -- final result = ', lowest_location)
