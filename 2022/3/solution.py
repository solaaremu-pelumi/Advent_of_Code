import os 
import logging

PRIORITY_MAPPING = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10, 
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26,
    'A' : 27,
    'B' : 28,
    'C' : 29,
    'D' : 30,
    'E' : 31,
    'F' : 32,
    'G' : 33,
    'H' : 34,
    'I' : 35,
    'J' : 36,
    'K' : 37,
    'L' : 38,
    'M' : 39,
    'N' : 40,
    'O' : 41,
    'P' : 42,
    'Q' : 43,
    'R' : 44,
    'S' : 45,
    'T' : 46,
    'U' : 47,
    'V' : 48,
    'W' : 49,
    'X' : 50,
    'Y' : 51,
    'Z' : 52,
}

def read_file(filename):
    result = []
    logging.info("Processing", filename)
    filename = os.path.join(os.path.dirname(__file__), filename)

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            result.append(line)
    return result

def process_rucksack(rucksacks):
    score = 0
    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        left_compartment = set(rucksack[:mid])
        right_compartment = set(rucksack[mid:])
        common = (left_compartment & right_compartment).pop()
        score += PRIORITY_MAPPING[common]
    return score

def process_rucksack_groups(rucksacks):
    score = 0
    a = b = c = None
    current_location = 0
    for rucksack in rucksacks:
        if current_location == 0:
            a = rucksack
            current_location = 1
        elif current_location == 1:
            b = rucksack
            current_location = 2
        elif current_location == 2:
            c = rucksack
            current_location = 0
            common = (set(a) & set(b) & set(c)).pop()
            score += PRIORITY_MAPPING[common]

    return score

def main(input):
    rucksacks = read_file(input)
    logging.info("processing rucksacks")
    result = process_rucksack(rucksacks)
    logging.info("The result of processing the ruckstacks is ", result)
    return result

if __name__ == '__main__':
    rucksack = read_file('input.txt')
    # rucksack = read_file('test.txt')
    # assert process_rucksack(rucksack) == 157
    # assert process_rucksack_groups(rucksack) == 70
    print(process_rucksack_groups(rucksack))