import os 
import logging

def read_file(filename):
    result = []
    logging.info("Processing", filename)
    filename = os.path.join(os.path.dirname(__file__), filename)

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            line = list(line)
            result.append(line)
    return result
    
def process_marker(trees):
    width = len(trees[0])
    height = len(trees)
    all_sides = 2 * (width + height) - 4
    count_sides = all_sides

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            view_directions = [check_left(trees, i, j), check_right(trees, i, j), check_up(trees, i, j), check_down(trees, i, j)]
            if True in view_directions:
                count_sides += 1
    return count_sides

def process_highest_scenic_score(trees):
    width = len(trees[0])
    height = len(trees)
    highest_score_seen = 0

    for i in range(height):
        for j in range(width):
            trees_sight = [get_trees_left(trees, i, j), get_trees_right(trees, i, j), get_trees_up(trees, i, j), get_trees_down(trees, i, j)]
            current = 1
            for item in trees_sight:
                current *= item
            if current > highest_score_seen:
                highest_score_seen = current

    return highest_score_seen

def get_trees_left(trees, i, j):
    a = j - 1
    if j == 0:
        return 0
    trees_seen = 1
    while a > 0:
        if int(trees[i][a]) >= int(trees[i][j]):
            return trees_seen
        trees_seen += 1
        a -= 1
    return trees_seen

def get_trees_right(trees, i, j):
    a = j + 1
    left_width = len(trees[0])
    
    if j == left_width - 1:
        return 0

    trees_seen = 1
    while a < left_width - 1:
        if int(trees[i][a]) >= int(trees[i][j]):
            return trees_seen
        trees_seen += 1
        a += 1
    return trees_seen

def get_trees_up(trees, i, j):
    a = i - 1
    trees_seen = 1
    if i == 0:
        return 0
    
    while a > 0:
        if int(trees[a][j]) >= int(trees[i][j]):
            return trees_seen
        trees_seen += 1
        a -= 1
    return trees_seen

def get_trees_down(trees, i, j):
    a = i + 1
    trees_seen = 1
    height = len(trees)

    if i == height - 1:
        return 0
    while a < height - 1:
        if int(trees[a][j]) >= int(trees[i][j]):
            return trees_seen
        trees_seen += 1
        a += 1
    return trees_seen

def check_left(trees, i, j):
    a = j - 1
    can_see = True
    while a >= 0:
        if int(trees[i][a]) >= int(trees[i][j]):
            return False
        a -= 1
    return can_see

def check_right(trees, i, j):
    a = j + 1
    can_see = True
    left_width = len(trees[0])
    while a < left_width:
        if int(trees[i][a]) >= int(trees[i][j]):
            return False
        a += 1
    return can_see

def check_up(trees, i, j):
    a = i - 1
    can_see = True
    
    while a >= 0:
        if int(trees[a][j]) >= int(trees[i][j]):
            return False
        a -= 1
    return can_see


def check_down(trees, i, j):
    a = i + 1
    can_see = True
    height = len(trees)
    while a < height:
        if int(trees[a][j]) >= int(trees[i][j]):
            return False
        a += 1
    return can_see

if __name__ == '__main__':
    # input = read_file('test.txt')
    input = read_file('input.txt')
    print(process_highest_scenic_score(input))
