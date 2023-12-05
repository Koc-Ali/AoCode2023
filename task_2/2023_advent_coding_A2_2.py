import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
# filename = "2023_advent_input_A2_1.txt"
# filename = "2023_advent_input_A2_1.sample.txt"

filename = "2023_advent_input_A2_2.txt"
# filename = "2023_advent_input_A2_2.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
sum_of_power_cubes = 0

# extract value out of line
def extract_game_id(line):
    g_id = 0

    # extract games info
    pos_game_id_end = line.find(':')
    game_text = line[:pos_game_id_end]
    g_id = game_text.strip().split()[1]
    return (g_id)
def determine_max_cubes(line):
    valid_g_id = True
    max_red_cubes = 0
    max_green_cubes = 0
    max_blue_cubes = 0

    # extract games info
    pos_game_id_end = line.find(':')
    extracted_games = line[pos_game_id_end+1:]
    games_list = extracted_games.split(';')
    # print(' game list = ', games_list)

    # check games regarding max values
    for game in games_list:
        # print('    -- game = ', game)
        cubes = game.split(',')
        # print('cubes = ', cubes)
        for cube in cubes:
            cube_detail = cube.split()
            if (cube_detail[1].find('red') != -1) and (int(cube_detail[0]) > max_red_cubes):
                max_red_cubes = int(cube_detail[0])
            if (cube_detail[1].find('green') != -1) and (int(cube_detail[0]) > max_green_cubes):
                max_green_cubes = int(cube_detail[0])
            if (cube_detail[1].find('blue') != -1) and (int(cube_detail[0]) > max_blue_cubes):
                max_blue_cubes = int(cube_detail[0])
    return (max_red_cubes, max_green_cubes, max_blue_cubes)

for line in file:
    fields = line.strip()
    print(fields)

    game_id = extract_game_id(fields)
    max_red, max_green, max_blue = determine_max_cubes(fields)
    print('current sum =', sum_of_power_cubes, ', current game id = ', game_id, ', max_red = ', max_red, ', max_green = ', max_green, ', max_blue =', max_green)
    sum_of_power_cubes += max_red*max_blue*max_green

# print final results
print('--- final result = ', sum_of_power_cubes)
