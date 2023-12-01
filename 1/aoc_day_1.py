# Advent of Code Day 1

import re

def replace_numbers_in_list(strings):
    num_dict = {
        "one": "o1e",
        "two": "t2i",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    def replace_numbers(s):
        for word, number in num_dict.items():
            s = re.sub(word, number, s, flags=re.IGNORECASE)
        return s

    return [replace_numbers(s) for s in strings]

def aocSolver(input_file, task=1):
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()
    lines = replace_numbers_in_list(lines) if task == 2 else lines
    numbers_per_line = [''.join(re.findall(r"\d+", line)) for line in lines]
    return sum([int(nl[0] + nl[-1]) for nl in numbers_per_line if len(nl) > 0])

if __name__ == '__main__':
    input_file = "1/input.txt"
    print(aocSolver(input_file))
    print(aocSolver(input_file, 2))