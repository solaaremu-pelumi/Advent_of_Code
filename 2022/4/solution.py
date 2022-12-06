import os 
import logging

def read_file(filename):
    result = []
    logging.info("Processing", filename)
    filename = os.path.join(os.path.dirname(__file__), filename)

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            result.append(line)
    return result

def process_assignments(assignments):
    score = 0
    for assignment_pair in assignments:
        [elf_a, elf_b] = assignment_pair.split(',')
        [elf_a_start, elf_a_end] = elf_a.split('-')
        [elf_b_start, elf_b_end] = elf_b.split('-')
        if int(elf_a_start) <= int(elf_b_start) <= int(elf_b_end) <= int(elf_a_end)or int(elf_b_start) <= int(elf_a_start) <= int(elf_a_end) <= int(elf_b_end):
            score += 1
    return score

def process_assignments_overlap(assignments):
    score = 0
    for assignment_pair in assignments:
        [elf_a, elf_b] = assignment_pair.split(',')
        [elf_a_start, elf_a_end] = elf_a.split('-')
        [elf_b_start, elf_b_end] = elf_b.split('-')
        if int(elf_a_end) >= int(elf_b_start) and int(elf_b_end) >= int(elf_a_start):
            score += 1
    return score
    
def main(input):
    assignments = read_file(input)
    logging.info("processing assignments")
    result = process_assignments(assignments)
    logging.info("The result of processing the ruckstacks is ", result)
    return result

if __name__ == '__main__':
    assignments_test = read_file('test.txt')
    assignments = read_file('input.txt')
    # assert process_assignments(assignments) == 2
    assert process_assignments_overlap(assignments_test) == 4
    # assert process_rucksack_groups(rucksack) == 70
    # print(process_assignments(assignments))
    print(process_assignments_overlap(assignments))