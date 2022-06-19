def anagrams(word1, word2):
    if len(word1.replace(" ", "")) != len(word2.replace(" ", "")):
        return False
        
    set_one = set(word1.lower())
    set_two = set(word2.lower())

    if set_one == set_two:
        return True
    else:
        return False

print(anagrams("New York Times", "monkeys write"))