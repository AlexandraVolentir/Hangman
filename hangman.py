# This would be a pretty nice hangman game

def updated_current_word(initial_word, current_word, letter):
    if current_word.isspace():
        for i in range(len(initial_word)):
            if initial_word[i] ==  letter:
                current_word[i] = letter
    return current_word

container = input("Enter your word/phrase: ").strip()
print("so \"" + container + "\" would be the phrase to guess for the player")

done = False
length = len(container)
k = 0
cur_word = " "*length;

while(k != 9): # 9 parts of the body which need to be drawn unless the player guesses the word before
    
    letter = input("guess " + str(k + 1) + " out of 9. enter a letter: ")
    if letter in container:
        print("Right guess!!")
        cur_word = updated_current_word(container, cur_word, letter)
        print(cur_word)

