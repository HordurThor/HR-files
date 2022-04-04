from words import Words
from ui import UI

class Wordle:

    def __init__(self):
        self.word = None
        self.guesses = 0
        self.max_guesses = 5
        self.word_length = 5
        self.guessed_words = ["_____", "     "] * self.max_guesses

    def run_program(self):
        running = True
        valid = True
        game_ui = UI()
        while running:
            game_ui.display_menu(valid)
            valid = True
            val = input("Choose an option: ")
            if val != None:
                val = val.lower()

            if val == "playd":
                self.change_to_defult()
                self.clear_board()
                self.play_game(game_ui)

            elif val == "playc":
                self.customize_game(game_ui)
                self.clear_board()
                self.play_game(game_ui)

            elif val == "add":
                self.add_word_to_bank()

            elif val == "quit":
                running = False
            else:
                valid = False

    def play_game(self, game_ui):
        word = Words(self.word_length)
        self.word = word.get_a_word().upper()
        valid = True
        playing = True
        while playing:
            game_ui.display_game(self.guessed_words, valid)
            playing = True
            valid = True
            guess, guess_check = self.get_guess()
            if guess.upper() == self.word:
                self.end_game(game_ui, True)
                playing = False

            elif self.guesses == self.max_guesses:
                self.end_game(game_ui, False)
                playing = False

            else:
                if guess_check != None: # guess and the guess check is added to guessed words list if guess was valid 
                    self.insert_guessed_word(guess, guess_check)  
                else:
                    valid = False


    def change_to_defult(self):
        self.max_guesses = 5
        self.word_length = 5


    def end_game(self, game_ui, won):
        if won:
            game_ui.display_end(True, self.word)
        else:
            game_ui.display_end(False, self.word)
        val = input("Play again? ")
        if val != None:
            val = val.lower()
        if val == "y":
            self.clear_board()
            self.play_game(game_ui)
        elif val == "n":
            return


    def customize_game(self, game_ui):
        valid = True
        customizing = True
        while customizing:
            game_ui.display_customize(valid)
            val = input("What to change? ")
            if val != None:
                val = val.lower()
            if val == "word":
                wlengh = input("Input word length: ")
                if wlengh.isnumeric():
                    self.word_length = int(wlengh)
                else: 
                    valid = False
            elif val == "guess":
                num_of_guesses = input("Input number of guesses: ")
                if num_of_guesses.isnumeric():
                    self.max_guesses = int(num_of_guesses)
                else: 
                    valid = False
            elif val == "exit":
                customizing = False
        

    def add_word_to_bank(self):
        wrds = Words(self.word_length)
        not_added = True
        while not_added:
            word = input("Write the word you want to add: ")
            valid = self.check_word(word)
            if valid:
                wrds.add_word(word)
                not_added = False
    

    def check_word(self, word):
        if word.isalpha():
            return True
        return False

    def clear_board(self):
        empty_word = "_" * self.word_length
        empty_guess_check = " " * self.word_length
        self.guessed_words = [empty_word, empty_guess_check] * self.max_guesses
        self.guesses = 0

    def insert_guessed_word(self, guess, guess_check):
        for i, string in enumerate(self.guessed_words):
            if string == "_"*self.word_length:
                self.guessed_words[i] = guess
            if string == " "* self.word_length:
                self.guessed_words[i] = guess_check
                return 


    def get_guess(self):
        guess = input('Your guess: ')
        guess_check = self.check_guess(guess)
        if guess_check != None:
            self.guesses += 1 
        return guess, guess_check


    def check_guess(self, guess):
        if len(guess) != self.word_length:
            return None
        if not guess.isalpha():
            return None
        # if the validity checks pass then make a string of correct caracters
        guess = guess.upper()
        word_guess = ["-"] * self.word_length
        word_temp = list(self.word)
        for i, char in enumerate(guess):
            if char == word_temp[i]:
                word_guess[i] = char.upper()
                # remove the found character from the temp word and the guess
                word_temp[i] = "-"
                guess[i].replace(char, "-")
        for i, char in enumerate(guess):
            if char != "-":
                if char in word_temp:
                    word_guess[i] = char.lower()
                    # remove the found character from the temp word
                    for i, char0 in enumerate(word_temp):
                        if char0 == char:
                            word_temp[i] = "-"
                            break
        return "".join(word_guess)

