max_red_cubes = 12
max_green_cubes = 13
max_blue_cubes = 14
possible_games_count = 0

def game_possible(string):
    #remove Game [id] from beginning of string
    remove_game_id = string.split(':')[1]
    #split into subsets of revealead cubes
    subsets = remove_game_id.split(';')
    #initialize cube count
    red_cubes = 0
    green_cubes = 0
    blue_cubes = 0
    #check for highest number of cubes in each subset and update the cube counts
    for subset in subsets:
        parts = subset.split(',')
        for part in parts:
            count = int(part.split()[0])
            if 'red' in part and count > red_cubes: 
                red_cubes = count 
            elif 'green' in part and count > green_cubes:
                green_cubes = count
            elif 'blue' in part and count > blue_cubes:
                blue_cubes = count

    power_of = red_cubes * green_cubes * blue_cubes
    return power_of
 



with open('input.txt', 'r') as file:
    for line in file:
        processed_line = line.strip()
        power_of = game_possible(processed_line)
        possible_games_count += power_of


print("Total power of:", possible_games_count)
