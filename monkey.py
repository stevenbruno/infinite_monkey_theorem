# OBJECTIVE: generate a random 28 char string, compare it to the target string,
#            score the generated string based on similarity to target, repeat the process until there is a 100% match
#            https://runestone.academy/runestone/static/pythonds/Introduction/DefiningFunctions.html

import random
import string


target = "methinks it is like a weasel" #target string to which we will compare our generated strings


def generate_string():
    test_string = []
    for i in range(28):
        test_string.append(random.choice(string.ascii_lowercase + " "))
    return test_string


def score_string(target_string, attempt):
    score = 0
    for i in range(len(target_string)):
        if target_string[i] == attempt[i]:
            score += 1
    return score


# repeatedly calls generate and score until there is a 100% match
def simulate_monkeys():
    counter = 0
    best_score = 0
    best_string = ""
    trial = generate_string()
    trial_score = score_string(target, trial)
    while trial_score != 28:
        trial = generate_string()
        trial_score = score_string(target, trial)
        counter += 1
        if trial_score > best_score:
            best_score = trial_score
            best_string = trial
        if counter % 1000 == 0:
            print("attempt number: %d\nbest score so far: %d\nbest string so far: %s"
                % (counter, best_score, best_string))
    print("found a perfect match!")

simulate_monkeys()










