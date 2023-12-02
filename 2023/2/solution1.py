#Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
#What is the sum of the IDs of those games?

# the bag contains AT LEAST the number of items of each colour that we have in the dictionary
def make_dictionary(game_array):
    dict_init = { "red": 0, "green": 0, "blue": 0}
    for item in game_array: 
        s = item.split(',') 
        #print(s)
        for stat in s: 
            #print(stat)
            for colour in dict_init.keys(): 
                if colour in stat: 
                    number = int(stat.split()[0])
                    if number > dict_init[colour]:
                        dict_init[colour] = number
    return dict_init

# if more cubes of a colour occur than in the given bag, the game is invalid
def dict_compare(game_dict, compare_dict): 
    for colour in game_dict.keys(): 
        if game_dict[colour] > compare_dict[colour]:
            return False
    return True 
         
def sum_all(f):
    with open (f) as file: 
        sum = 0
        for line in file: 
            string = line.rstrip()
            print(string)
            id = int(string.split()[1].rstrip(":"))
            games = string.split(":")[1].split(";")

            game_dict = make_dictionary(games)

            compare_dict = {'red': 12, 'green': 13, 'blue': 14}

            if (dict_compare(game_dict, compare_dict)):
                sum += id
    return sum