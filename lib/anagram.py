# lib/anagram.py
# Define the Anagram class
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store the word in lowercase to handle case insensitivity

    def match(self, word_list):
        # Sort the original word
        sorted_word = sorted(self.word)
        
        # Find matches by comparing sorted versions of words
        matches = []
        for candidate in word_list:
            if sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)
        
        return matches

# Create an instance of the Anagram class
anagram_checker = Anagram("listen")


possible_anagrams = ['enlist', 'hippopotamus', 'inlets', 'poison','silent']


print(anagram_checker.match(possible_anagrams))
