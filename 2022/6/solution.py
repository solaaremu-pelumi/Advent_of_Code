import os 
import logging

def read_file(filename):
    result = []
    logging.info("Processing", filename)
    filename = os.path.join(os.path.dirname(__file__), filename)

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            return line

def process_marker(datastream, length_of_distinct_characters=4):
    left = right = 0
    for char in datastream:
        if right - left == length_of_distinct_characters:
            return right
        elif char in datastream[left:right]:
            left = datastream.index(char, left, right) + 1
            right += 1
        else:
            right += 1

if __name__ == '__main__':
    # input = read_file('test.txt')
    input = read_file('input.txt')
    # assert read_file('test.txt') == "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    # assert process_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    # assert process_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    # assert process_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
    # assert process_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    # assert process_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    print(process_marker(input))
    print(process_marker(input, 14))