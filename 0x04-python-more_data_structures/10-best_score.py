#!/usr/bin/python3
def best_score(a_dictionary):
    max_val = 0
    winner = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > max_val:
                max_val = value
                winner = key
    return winner
