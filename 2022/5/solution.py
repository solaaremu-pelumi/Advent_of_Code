import os 
import logging

def read_file(filename):
    moving_instructions = []
    logging.info("Processing", filename)
    filename = os.path.join(os.path.dirname(__file__), filename)

    with open(filename) as f:
        reading_moving_instructions = False
        first = True
        for original_line in f:
            line = list(original_line)
            length_of_line = len(line)
            if first:
                count_of_columns = int((length_of_line) / 4)
                original_stacking = [ [] for i in range(count_of_columns)]
                first = False
            if len(line) <= 3: 
                reading_moving_instructions = True
            elif not reading_moving_instructions:
                pointer = 0
                row = 0
                while pointer < length_of_line:
                    if line[pointer] == '[':
                        original_stacking[row].append(line[pointer+1])
                    row += 1
                    pointer += 4
            elif reading_moving_instructions:
                temp = []
                line = original_line.rstrip().split(' ')
                for item in line:
                    if item.isdigit():
                        temp.append(item)
                moving_instructions.append(temp)

    return original_stacking, moving_instructions

def process_top_stack(stack, instructions):
    for [count, source, destination] in instructions:
        count, source, destination = int(count), int(source) - 1, int(destination) -1
        for _ in range(count):
            stack[destination] = [stack[source][0]] + stack[destination]
            stack[source] = stack[source][1:]
    result = ''
    for i in range(len(stack)):
        result += stack[i][0]

    return result

def process_top_stack_in_order(stack, instructions):
    for [count, source, destination] in instructions:
        count, source, destination = int(count), int(source) - 1, int(destination) -1
        stack[destination] = stack[source][0:count] + stack[destination]
        stack[source] = stack[source][count:]

    result = ''
    for i in range(len(stack)):
        result += stack[i][0]

    return result
    
if __name__ == '__main__':
    # original_stacking, moving_instructions = read_file('test.txt')
    original_stacking, moving_instructions = read_file('input.txt')
    # assert process_top_stack(original_stacking, moving_instructions) == 'CMZ'
    # assert process_top_stack_in_order(original_stacking, moving_instructions) == 'MCD'
    # assert process_assignments_overlap(assignments_test) == 4
    # assert process_rucksack_groups(rucksack) == 70
    # print(process_assignments(assignments))
    # print(process_top_stack(original_stacking, moving_instructions))
    print(process_top_stack_in_order(original_stacking, moving_instructions))


'''
I want an stack for each of the entries

array = [[N,Z], [D,C,M], [P]]
for line in array:
    pointer = 0
    row = 0
    if line[0] == ' ':
        pointer += 4
        row += 1
    if line[]
column_0 = [N, Z]
column_1 = [D, C, M]
column_3 = [P]

I want the moving instructions to be like

instructions = [(count, source, destination)]
'''