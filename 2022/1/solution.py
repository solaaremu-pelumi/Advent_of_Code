import os 
import logging
from heapq import heappop, heappush, heapify


def read_file(filename):
    result = []
    logging.info("Processing", filename)
    filename = os.path.join(os.path.dirname(__file__), filename)

    with open(filename) as f:
        for line in f:
            result.append(line.rstrip())
    return result

def process_calories(calories, response = "largest"):

    heap = []
    heapify(heap)
    heappush(heap, 0)
    heappush(heap, 0)
    heappush(heap, 0)

    len_of_calories = len(calories)
    current_calorie_count = 0

    for index, calorie in enumerate(calories):
        if calorie.isdigit():
            current_calorie_count += int(calorie)

        if index == len_of_calories - 1 or calorie == "" :
            if current_calorie_count > heap[0]:
                heappop(heap)
                heappush(heap, current_calorie_count)
            current_calorie_count = 0

    if response == "largest":
        return heap[1]
    elif response == "largest-3":
        return sum(heap)


def main(input):
    calories = read_file(input)
    logging.info("processing calories")
    largest_calorie = process_calories(calories)
    logging.info("The Largest Calorie is", largest_calorie)
    sum_largest_3_calories = process_calories(calories, "largest-3")
    return largest_calorie, sum_largest_3_calories

if __name__ == '__main__':
    print(main('input.txt'))
    # assert main('test.txt') == (24000, 45000)