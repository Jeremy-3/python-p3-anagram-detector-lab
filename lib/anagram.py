# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word.lower())
    def match(self,possible_anagram):
        matches = []
        
        for word in possible_anagram:
            if sorted(word.lower()) == self.sorted_word:
                matches.append(word)        

        return matches    

   