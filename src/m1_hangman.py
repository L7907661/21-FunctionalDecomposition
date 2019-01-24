"""
Hangman.

Authors: Zeyu Liao and Chen Li.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# done: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random
def main():
    print('I will choose a random secret word from a dictionary.'
          'You will set the MINIMUM length of that word')
    N = mm_length()
    M = wrong_words()
    print('You set the DIFFICULTY of the game by setting the number of unsuccessful choices you can make before'
          'you LOSE the game')
    print('Here is what you currently know about the secret word:')
    words = word(N)
    empty = list(len(words) * '-')
    print(empty)
    hangman(words,M)
    play()

def mm_length():
    print('What MINIMUM length do you want for the secret word ?')
    N = input()
    return N
def wrong_words():
    print('How many unsuccessful choices do you want to allow yourself?')
    M = input()
    return M
def word(N):
    while True:
        with open('words.txt') as f:
            string = f.read()
            aa = string.split()
            r = random.randrange(0,len(aa))
            words = aa[r]
            if int(len(words)) >= int(N):
                break
    return words

def hangman(words,M):
    empty = list(len(words) * '-')
    wrongtime = int(M)
    while True:
        print(' What letter do you want to try?')
        letter = input()
        if letter in words:
            for i in range(len(words)):
                if letter == words[i]:
                    empty[i] = letter
            print('Your succeed')
        else:
            wrongtime = wrongtime -1
            print("Sorry, there is no", letter, 'in the secret word. ')
        print('here is what you currently know about the secret word:')
        print(empty)
        if '-' not in empty:
            return print('Your succeed :)')
        if wrongtime == 0:
            return print(' You lose!','The secret word was:',words)
        print('You can still try', wrongtime, 'times')


def play():
    print('PLay another game? (y/n)')
    A = input()
    if A == 'y':
        main()








main()


