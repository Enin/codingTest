# You are given a dictionary of words and a large input string.
# You have to find out whether the input string can be completely segmented into the words of a given dictionary.
# The following two examples elaborate on the problem further.
import collections
# recursion과 memoization을 사용

given_dict = ['apple', 'apple', 'pear', 'pie']
input_string = ['applepie', 'applepeer']

def can_segment_string(str, dict):
    for s in range(1, len(str)+1):
        first_word = str[0:s]
        if first_word in dict:
            second_word = str[s:]
            if not second_word or second_word in dict or can_segment_string(second_word, dict):
                return True
    return False

def test():

    dict_set = set(given_dict)
    if can_segment_string(input_string[1], dict_set):
        print("Input string can be segmented")
    else:
        print("Input string can't be segmented")

test()

