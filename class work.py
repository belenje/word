max_attempt=5
import random
Word_LIST=['name','car','plane','dog','stuff']
import random
def pick_word(listword):
    return random.choice(listword)
def get_guess():
    guess=input('guess a word:')
    if not guess =='':
        return guess
    else:
        print('words cannot be empty')
get_guess()
def evaluate_guess(attempts_list):
    word =pick_word(WORD_LIST)
    if attempts_left == max_attempts:
         word == word
    else:
         word = pick_word(WORD_LIST)
    if guess == word:
         return True
         print('your answer is correct')
    else:
         return False
         print('try again')
        
def play_game():
    if evaluate_guess==True:
        print("your guess is correct")
        resp =input ("do you want to play again? Y/N")
        if resp =="y" :
            play_game()      
        else :
            print("goodbye")

play_game()            




    
##    print("welcome to the SWITCH Master Guess game")
##    game_count= 5
##    attempts= 0
##    max _attempt= 5
##    while game_count> 0:
##    game_count-=1
##    while evaluate_guess():



    
