import random
file_name = 'words.txt'

def guess_word():
    guess = input("Enter the word please :')
    return guess

def load_word():
    word = open(file_name,'r',)
    line = word.readline()
    wordlist = line.split()
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)

def play_again():
    game_status = input("\t \t Do you want to play again? :").upper()
    game_status = game_status[0]
    
    if game_status == "Y":
        return main()
    elif game_status == "N":
        return False
    else:
        return False



def main():
    guess_try = 5
    guessed_try = 0
    load_word()
    wordlist = load_word()
    word = choose_word(wordlist)

    while True and guess_try >= 0:
        

##            print(word)
        guessed_try += 1
        print("""\t I picked a word and i want you to try guessing it.
              The word is of {x} character, you've {y} try!!!""".format(y=guess_try, x=len(word)))
        guess = guess_word()
        guess_try -= 1

        if guess_try == 0:
            print("\t \t \t \t Game Over!!!. The word is {x}".format(x=word))
            return play_again()
            
            
        elif guess == word:
            print("\t You got it right in {y} try. The word is {x}".format(y=guessed_try, x = word))

            return play_again()
        
        

main()
