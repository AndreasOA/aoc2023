# Advent of Code Day 2

def aocSolver(input_file, req, task=1):
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()
    valid_games = 0
    power_sum = 0
    for line in lines:
        game, content = line.split(": ")
        game_id = int(game.replace("Game ", ""))
        pulls = content.split("; ")
        valid = True
        pull_dict = {}
        for pull in pulls:
            if not valid:
                break
            for pull_val in pull.split(", "):
                value, color = pull_val.split(" ")
                value = int(value)
                color = color.replace("\n", "")
                try:
                    if pull_dict[color] < value:
                        pull_dict[color] = value
                except KeyError:
                    pull_dict[color] = value
                if task == 1:
                    if color not in req:
                        valid = False
                        break
                    elif req[color] < value:
                        valid = False
                        break
        power = 1
        for key, value in pull_dict.items():
            power *= value
        power_sum += power
        if valid:
            valid_games += game_id
    if task == 1:
        return valid_games
    else:
        return power_sum
                        



if __name__ == '__main__':
    req_t1 = {"red": 12, "green": 13, "blue": 14}
    input_file = "2/input.txt"
    print(aocSolver(input_file, req_t1))
    print(aocSolver(input_file, req_t1, task=2))
