import random
import csv
class Word:
    def __init__(self):
        self.word = None
        self.lword = None
        self.uword = None
        self.wordlist = []
        self.loadcsv()
    def pickword(self):

        num = random.randint(0, len(self.wordlist)-1)
        self.word = self.wordlist[num]
        self.lword = self.word.lower()
        self.uword = ["_"] * len(self.word)
    def loadcsv(self):
        with open('Words.csv') as wordlist:
            readCSV = csv.reader(wordlist, delimiter="\n")
            for word in readCSV:
                self.wordlist.append(word[0])
Hangw = Word()
Hangw.pickword()
class Game:
    def __init__(self, human=True):
        self.word = Hangw.word
        self.lword = self.word.lower()
        self.uword = ["_"] * len(self.word)
        if " " in self.word:
            for letter in range(0, len(self.word)):
                if self.word[letter] == " ":
                    self.uword[letter] = ' '
        self.human = human
        self.diff = None
        self.bank = []
        self.wordg = None


    def setup(self):
        while True:
            x = input("Do you want to play an AI (type yes or no): ")
            if x.lower() == "yes":
                self.human = False
                break
            elif x.lower() == "no":
                break
            else:
                print("Please enter yes or no")


        while True:
            try:
                diff = int(input("How many guesses would you like: "))
            except ValueError:
                print("Must be a number")
            else:
                break
        if diff <= 0:
            print("That doesnt work buddy")
        self.diff = diff
    def set_word(self):
        word = input("Gimme a word boy: ")
        return word

    def check(self):
        if "_" not in self.uword:
            print("".join(self.uword))
            print("you won! nice!")
            return True
        elif self.diff <= 0:
            print("you lost NERD")
            print(f"The Correct Word: {self.word}")
            return True



    def guess(self):
        print("\n")
        print("".join(self.uword))

        print("you have %s more guesses" % (str(self.diff)))
        guess = str(input("Gimme a letter, boy: "))
        guess = guess.lower()
        if guess == self.word.lower():
            for letter in range(0, len(self.word)):
                    self.uword[letter] = self.word[letter]
            self.wordg = True
        elif guess in self.bank:
            print("you've already guessed this letter")
        elif guess in self.lword:
            for letter in range(0, len(self.word)):
                if self.lword[letter] == guess:
                    self.uword[letter] = self.word[letter]
            self.bank.append(guess)
        elif guess == self.word:
            self.wordg = True
        else:
            self.diff -= 1
            print("No")

    def run(self):
        self.setup()
        if self.human:
            self.word = self.set_word()
            self.lword = self.word.lower()
            self.uword = ["_"] * len(self.word)
            if " " in self.word:
                for letter in range(0, len(self.word)):
                    if self.word[letter] == " ":
                        self.uword[letter] = ' '
        elif not self.human:
            pass
        while True:
            self.guess()
            if self.check():
                break
game = Game()
game.run()










