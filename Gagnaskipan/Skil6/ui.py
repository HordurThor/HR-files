class UI:

    def __init__(self):
        self.header = """
          _ _ _ _____ _____ ____  __    _____ 
         | | | |     | __  |    \|  |  |   __|
         | | | |  |  |    -|  |  |  |__|   __|
 ________|_____|_____|__|__|____/|_____|_____|________
|                                                     |"""
        self.word_field = "|                        {}                        |\n"
        self.footer = """|_____________________________________________________|"""



    def display_menu(self, valid=True):
        inval = "                "
        if not valid:
            inval = "Input is invalid"
        print(self.header)
        print(f"""|                                                     |
|                                                     |
|                Play defult game[playd]              |
|                Play custom game[playc]              |
|             Add new word to word bank[add]          |
|                      Quit[quit]                     |
|                                                     |
|                   {inval}                  |
|                                                     |""")
        print(self.footer)

    def display_game(self, guessed_list, valid=True):
        inval = "              "
        if not valid:
            inval = "Invalid format"
        
        print(self.header)
        fields = self.word_field * len(guessed_list)
        print(fields.format(*guessed_list))
        print("""|                   {}                    |
|                    Take a guess                     |""".format(inval))
        print(self.footer)


    def display_customize(self, valid=True):
        inval = ""
        if not valid:
            inval = "Has to be number"
        print(self.header)
        print(f"""|                                                     |
|                  Change word lenght[word]           |
|                  Change number of guesses[guess]    |
|                  Exit[exit]                         |
|                            {inval}                  |
|                                                     |""")
        print(self.footer)


    def display_end(self, won, word):
        end_str = ''
        if won:
            end_str = 'You guessed the word!       '
        else:
            end_str = "You didn't guess the word :("

        print(self.header)
        print("""|                                                     |
|                {}         |
|                    The word was:                    |
|                       {}                         |
|                   play again? (y/n)                 |""".format(end_str, word.upper()))
        print(self.footer)

