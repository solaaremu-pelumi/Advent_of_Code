import os
import copy 
import logging

def read_file(filename):
    base_structure = {'files': [], 'directories': {}, 'size': 0}
    file_represetation = {'files': [], 'directories': {'/': copy.deepcopy(base_structure)}, 'size': 0}
    directory_stack = []
    score_stack = []
    all_scores = []
    logging.info("Processing", filename)
    filename = os.path.join(os.path.dirname(__file__), filename)

    with open(filename) as f:
        current_directory = None
        for line in f:
            line = line.rstrip()
            line = line.split(' ')
            if line[-1] == '..':
                file_represetation = deep_update_directory_size(directory_stack, file_represetation, score_stack[-1])
                # file_represetation['directories'][current_directory]['size'] = current_sum
                directory_stack.pop()
                score_stack[-2] += score_stack[-1]
                all_scores.append(score_stack.pop())
            elif 'cd' in line:
                directory_stack.append(line[-1])
                score_stack.append(0)
            elif 'ls' in line:
                current_directory = directory_stack[-1]
            else:
                if 'dir' in line:
                    file_represetation = deep_find_directory(directory_stack, file_represetation, copy.deepcopy(base_structure), line[-1])
                else:
                    size = int(line[0])
                    file_represetation = deep_update_directory(directory_stack, file_represetation, size, line[-1])
                    score_stack[-1] += size
    
    unprocessed = len(score_stack) - 1
    while unprocessed >= 0:
        if unprocessed == 0:
            all_scores.append(score_stack.pop())
        else:
            score_stack[unprocessed - 1] += score_stack[unprocessed]
            all_scores.append(score_stack.pop())
        unprocessed -= 1
    # return file_represetation
    return all_scores

def deep_find_directory(stack, file_represetation, item, index):
    current_directory = file_represetation
    for directory in stack:
        current_directory = current_directory['directories'][directory]
    current_directory['directories'][index] = item
    return file_represetation

def deep_update_directory(stack, file_represetation, size, index):
    current_directory = file_represetation
    for directory in stack:
        current_directory = current_directory['directories'][directory]
    current_directory['files'].append([index, size])
    return file_represetation

def deep_update_directory_size(stack, file_represetation, size):
    current_directory = file_represetation
    for directory in stack:
        current_directory = current_directory['directories'][directory]
    current_directory['size'] = size
    return file_represetation

def find_smallest_3_less_than_100(sizes):
    new_size = sorted(sizes)
    sum = 0
    for item in new_size:
        if item < 100000:
            sum += item
        else:
            return sum
    return sum

def find_single_largest_required_directorys(sizes):
    new_size = sorted(sizes)
    file_usage = new_size[-1]
    required = 70000000 - file_usage
    new_required = 30000000 - required
    for index, item in enumerate(new_size):
        if item > new_required:
            return item

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
    # assert find_smallest_3_less_than_100(input) == 95437
    # print(find_smallest_3_less_than_100(input))
    print(find_single_largest_required_directorys(input))
'''
    build the tree

    {
        '/': {'a': 'files': [[(b.txt, size), (c.dat. size)], size: 0,j directories: {} ), 'b': {}, 'c': {}},
    }

    split the line if it has 'cd' choose the last as the diretory being explored

    then post ls
    
    store curent node being explored
    if it has dir in it, create a directory on that node.

    create a stack of the nodes

    ['/']

    if it is a '..' pop the stack

    0l

'''