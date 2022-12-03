import os 
import logging

CHOICE_SCORE_MAPPING = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

ROUND_RESULT_MAPPING = {
    ('A', 'X') : 'draw',
    ('A', 'Y') : 'win',
    ('A', 'Z') : 'lose',
    ('B', 'X') : 'lose',
    ('B', 'Y') : 'draw',
    ('B', 'Z') : 'win',
    ('C', 'X') : 'win',
    ('C', 'Y') : 'lose',
    ('C', 'Z') : 'draw',
} 

REQUIRED_CHOICE_MAPPING = {
    ('A', 'X') : 'Z',
    ('A', 'Y') : 'X',
    ('A', 'Z') : 'Y',
    ('B', 'X') : 'X',
    ('B', 'Y') : 'Y',
    ('B', 'Z') : 'Z',
    ('C', 'X') : 'Y',
    ('C', 'Y') : 'Z',
    ('C', 'Z') : 'X',
}

RESULT_SCORE_MAPPING = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def read_file(filename):
    result = []
    logging.info("Processing", filename)
    filename = os.path.join(os.path.dirname(__file__), filename)

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            result.append(line.split())
    return result

def check_play_result(opp, player):
    return ROUND_RESULT_MAPPING[(opp, player)]

def check_required_play(opp, result):
    return REQUIRED_CHOICE_MAPPING[(opp, result)]

def process_strategy(strategy):
    score = 0

    for [opp, player] in strategy:
        score += CHOICE_SCORE_MAPPING[player]
        result = check_play_result(opp, player)
        if  result == 'win':
            score += 6
        elif result == 'draw':
            score += 3

    return score

def process_required_choices_score(strategy):
    score = 0

    for [opp, result] in strategy:
        score += RESULT_SCORE_MAPPING[result]
        required_play = check_required_play(opp, result)
        score += CHOICE_SCORE_MAPPING[required_play]
    return score

def main(input):
    strategy = read_file(input)
    logging.info("processing strategy")
    result = process_required_choices_score(strategy)
    logging.info("The result of the strategy is ", result)
    return result

if __name__ == '__main__':
    print(main('input.txt'))
    # assert main('test.txt') == 12