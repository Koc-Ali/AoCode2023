import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2023_advent_input_A2_1.txt"
# filename = "2023_advent_input_A2_1.sample.txt"

# filename = "2023_advent_input_A2_2.txt"
# filename = "2023_advent_input_A2_2.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
sum_of_valid_game_ids = 0
max_red_cubes = 12
max_green_cubes = 13
max_blue_cubes = 14

# extract value out of line
def extract_game_id(line):
    g_id = 0

    # extract games info
    pos_game_id_end = line.find(':')
    game_text = line[:pos_game_id_end]
    g_id = game_text.strip().split()[1]
    return (g_id)
def verify_games(line):
    valid_g_id = True
    valid_red = True
    valid_green = True
    valid_blue = True

    # extract games info
    pos_game_id_end = line.find(':')
    extracted_games = line[pos_game_id_end+1:]
    games_list = extracted_games.split(';')
    # print(' game list = ', games_list)

    # check games regarding max values
    for game in games_list:
        # print('    -- game = ', game)
        if (valid_blue == True) and (valid_red == True) and (valid_green == True):
            cubes = game.split(',')
            # print('cubes = ', cubes)
            for cube in cubes:
                cube_detail = cube.split()
                if (valid_blue == True) and (valid_red == True) and (valid_green == True):
                    if (cube_detail[1].find('red') != -1) and (int(cube_detail[0]) > max_red_cubes):
                        valid_red = False
                        return (False)
                    if (cube_detail[1].find('blue') != -1) and (int(cube_detail[0]) > max_blue_cubes):
                        valid_blue = False
                        return (False)
                    if (cube_detail[1].find('green') != -1) and (int(cube_detail[0]) > max_green_cubes):
                        valid_green = False
                        return (False)
    return (valid_g_id)

for line in file:
    fields = line.strip()
    print(fields)

    game_id = extract_game_id(fields)
    game_id_valid = verify_games(fields)
    print('current sum =', sum_of_valid_game_ids, ', current game id = ', game_id, ', valid = ', game_id_valid)
    if game_id_valid == True:
        sum_of_valid_game_ids += int(game_id)

# print final results
print('--- final result = ', sum_of_valid_game_ids)
