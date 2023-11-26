import string, random

############# INITIALISATION ##############

word = open("Words.txt")
word_list = word.read().split(" ")
#print(len(word_list))
word.close()

random_number = random.randint(0, len(word_list))
answer = str(word_list[random_number])
answer = answer[0:len(answer)-1]
#answer = "feel"    ###DEBUG
sheet = ""
for i in answer:
    sheet += "_"
#print(answer, len(sheet))

possible_letters = list(string.ascii_letters)
guessed_letters = []
lives = 7
initial = True

###########################################
def hangman():
    print(lives, "lives remaining")
    return

def check(letter):
    if letter in answer:
        global sheet, guessed_letters
        indexes = list_duplicates_of(answer,letter)
        #print(indexes)
        
        for i in indexes:
            sheet1 = sheet[:i]
            sheet2 = sheet[i+1:]
            sheet = sheet1 + letter + sheet2
            
        print("Good job, you guessed a letter!", "The word is", sheet)

        guessed_letters.append(letter.upper())
        possible_letters.remove(letter)
        possible_letters.remove(letter.upper())
        #print(possible_letters)
        if sheet != answer:
            print("You have guessed:", guessed_letters)
            guess()
        else:
            print("Congratulations, you solved the answer!")
            return
        
    else:
        guessed_letters.append(letter.upper())
        possible_letters.remove(letter)
        possible_letters.remove(letter.upper())

        global lives
        lives -= 1
        if lives == 0:
            print("No more lives, you have failed. The answer is '" + answer + "'.")
        else:
            print("Letter is not found in answer, try again!")
            hangman()
            print("You have guessed:", guessed_letters)
            print("The word is:", sheet)

            guess()
    return

def guess():
    global initial
    if initial:
        print("The word is:", sheet)
        initial = False
    letter = input("What letter would you like to guess? ")
    #print(type(letter))
    if len(letter) != 1:
        print("Error, you can only guess a letter in the alphabet.")
        guess()
    elif letter not in possible_letters:
        print("It looks like you have already guessed", letter.lower(), "before. Try another letter.")
        guess()
    else:
        #print("Valid Letter")
        check(letter.lower())

def list_duplicates_of(seq,item):  #Fix multiple of the same letter
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

guess()