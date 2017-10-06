word= input("Type the word you want to reverse:  ")
wordlist = []
rev_word = []
def reverse_word():
    for item in word:
        wordlist.append(item)
    print(' '.join(wordlist))
    i=-1
    for item in word:
        rev_word.append(word[i])
        i-=1
    print(' '.join(rev_word))
    

reverse_word()
