# String cleaning
# ===============

# Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists who are turning rabbits into zombies. He sends a text transmission to you, but it is intercepted by a pirate, who jumbles the message by repeatedly inserting the same word into the text some number of times. At each step, he might have inserted the word anywhere, including at the beginning or end, or even into a copy of the word he inserted in a previous step. By offering the pirate a dubloon, you get him to tell you what that word was. A few bottles of rum later, he also tells you that the original text was the shortest possible string formed by repeated removals of that word, and that the text was actually the lexicographically earliest string from all the possible shortest candidates. Using this information, can you work out what message your spy originally sent?

# For example, if the final chunk of text was "lolol," and the inserted word was "lol," the shortest possible strings are "ol" (remove "lol" from the beginning) and "lo" (remove "lol" from the end). The original text therefore must have been "lo," the lexicographically earliest string.

# Write a function called answer(chunk, word) that returns the shortest, lexicographically earliest string that can be formed by removing occurrences of word from chunk. Keep in mind that the occurrences may be nested, and that removing one occurrence might result in another. For example, removing "ab" from "aabb" results in another "ab" that was not originally present. Also keep in mind that your spy's original message might have been an empty string.

# chunk and word will only consist of lowercase letters [a-z].
# chunk will have no more than 20 characters.
# word will have at least one character, and no more than the number of characters in chunk.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
#
# Test cases
# ==========

# Inputs:
#     (string) chunk = "lololololo"
#     (string) word = "lol"
# Output:
#     (string) "looo"

# Inputs:
#     (string) chunk = "goodgooogoogfogoood"
#     (string) word = "goo"
# Output:
#     (string) "dogfood"

import re
from collections import deque

# Finds the start and end of matches in string
def find_all(string, sub):
    start = 0
    while True:
        start = string.find(sub, start)
        if start > -1:
            yield (start, start+len(sub),)
            start += 1
        else:
            break

def answer(chunk, word):
    # Check simple case (no match for word in chunk)
    regex_check = re.compile(word)
    if not regex_check.search(chunk):
        return chunk
        
    final_result = chunk
    possible_strings = deque([chunk])
    previously_checked = set()

    # Loop through possible_strings to find best possible result
    # Add new matches to possible_strings
    while len(possible_strings):
        temp = possible_strings.popleft()
        matches = find_all(temp, word)
        for start, end in matches:
            result = temp[:start] + temp[end:]
            if result in previously_checked:
                continue
            elif len(result) == len(final_result):
                final_result = min(result, final_result)
            elif len(result) < len(final_result):
                final_result = result
            previously_checked.add(result)
            possible_strings.append(result)
    return final_result