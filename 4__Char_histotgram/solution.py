from collections import Counter

def char_histogram(string):
    counter = Counter(string)
    return dict(counter)

char_histogram('Python!')


def char_histogram2(string):
    counter = {}
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

char_histogram2('Python!')