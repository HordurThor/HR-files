import random

class Words:
    
    def __init__(self, len_of_words):
        self.words = []
        self.file = open('words_bank', 'r+')
        for word in self.file:
            word = word.strip()
            if len(word) == len_of_words:
                self.words.append(word)


    def get_a_word(self):
        rand_index = random.randint(0, len(self.words))
        word = self.words[rand_index]
        return word

    def add_word(self, word):
        if word in self.words:
            return
        self.file.write(word+"\n")