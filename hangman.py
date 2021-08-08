# This would be a pretty nice hangman game

def updated_current_word(initial_word, current_word, letter):
    if '*' in current_word:
        for i in range(len(initial_word)):
            if initial_word[i] ==  letter:
                current_word[i] = letter
    return current_word

content = ["Animals", "Home utilities", "Clothes", "Food", "Jobs",
           "Body", "Computer", "Personal", "Sports", "Kitchen", 
           "Bathroom", "Nature", "Stationery", "Music", "Transport", 
           "Healthcare", "Buildings", "Places/Landscapes", 
           "Numbers", "Countries",  "Garden", "Things", "Pool"
            "Colors"]

done = False
while not(done):
    cathegory = input("-------------Please choose your cathegory: -------------------\n" + " ".join(content) + "\nYour cathegory is: ").capitalize();
    done = cathegory.capitalize() in content
    if not(done):
        print("You entered an unexisting cathegory. try again: ")
str_container = input("Enter your word/phrase: ").strip().lower()
container = list(str_container)
print("so \"" + str_container + "\" would be the phrase to guess\n-------------------------\n")

done = False
length = len(str_container)
k = 0
cur_word = list("*"*length);

while(k != 9 ): # 9 parts of the body which need to be drawn unless the player guesses the word before
    if '*' in cur_word:
        letter = input(str(9 - k) + " guesses left! enter a letter: ")[:1]
        if letter in container:
                if letter in cur_word:
                    print("You already guessed that letter. try again")
                    continue
                print("Right guess!!")
                cur_word = updated_current_word(container, cur_word, letter)
                print("".join(cur_word))     
        else:
            print("Wrong guess!")
            k += 1
    else:
            print("You guessed the word!\n Felicitas!")
            break
