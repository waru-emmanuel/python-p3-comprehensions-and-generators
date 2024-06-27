#!/usr/bin/env python3

def return_evens(num_list):
    """Returns a list of even numbers from a list of integers."""

    return [num_list[i] for i in range(len(num_list)) if num_list[i] % 2 == 0]

'''The function uses a list comprehension to iterate over the indices of the input list (range(len(num_list))) 
and checks if the number at the current index is even (num_list[i] % 2 == 0).'''


def make_exclamation(sentence_list):
    """Returns a list of sentences with exclamation marks."""

    return [sentence_list[i] + "!" for i in range(len(sentence_list))]

'''The function uses a list comprehension to iterate over the indices of the input list (range(len(sentence_list))) and creates a new list by concatenating each sentence with an exclamation mark (sentence_list[i] + "!"). 
    The resulting list is then returned by the function'''
    