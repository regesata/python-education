import os
import random
import re


def find_all(main_string: str, find_item: str) -> list:
    """ Function search for all occurrences of find_item
        in main_string and returns list with indexes"""
    res_list = []
    for i in range(len(main_string)):
        if main_string[i].lower() == find_item.lower():
            res_list.append(i)
    return res_list


def draw_hangman(lifes: int):
    """ Draw hangman using ascii symbols.
        Picture depends of lifes """
    os.system("clear")
    if lifes == 0:
        print("    ______")
        print("    |    |")
        print("    |    @")
        print("    |   /|\\")
        print("    |    |")
        print("    |   / \\")
        print("____|____")
    elif lifes == 1:
        print("    ______")
        print("    |    |")
        print("    |    @")
        print("    |   /|\\")
        print("    |    |")
        print("    |     \\")
        print("____|____")
    elif lifes == 2:
        print("    ______")
        print("    |    |")
        print("    |    @")
        print("    |   /|\\")
        print("    |    |")
        print("    |    ")
        print("____|____")
    elif lifes == 3:
        print("    ______")
        print("    |    |")
        print("    |    @")
        print("    |   /|\\")
        print("    |    ")
        print("    |    ")
        print("____|____")
    elif lifes == 4:
        print("    ______")
        print("    |    |")
        print("    |    @")
        print("    |   /|")
        print("    |    ")
        print("    |    ")
        print("____|____")
    elif lifes == 5:
        print("    ______")
        print("    |    |")
        print("    |    @")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("____|____")
    elif lifes == 6:
        print("    ______")
        print("    |    |")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("____|____")
    elif lifes == 7:
        print("    ______")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("____|____")
    elif lifes == 8:
        print("     ")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("____|____")
    elif lifes == 9:
        print("    ")
        print("    ")
        print("    ")
        print("    ")
        print("    ")
        print("____|____")
    elif lifes == 10:
        return


def pick_word() -> str:
    """Pick random word from file.
       Word is not used if it were in game"""
    if not os.path.isfile("used_words.txt"):  # create file "used_words if it isn`t exists"
        open("used_words.txt", "w").close()

    with open("used_words.txt") as used_words_file, open("words_list.txt") as words_file:
        used_word_list = used_words_file.readlines()
        word_list = words_file.readlines()
        while True:
            result_string = random.choice(word_list)
            if result_string not in used_word_list:
                return result_string.strip()


def show_used_words():
    """This function shows used_words.txt file"""
    os.system("clear")
    print("Words used in earlier games:\n")
    if not os.path.isfile("used_words.txt"):
        print("No one words in file\n")
    else:
        with open("used_words.txt") as used_words_file:
            used_words_list = used_words_file.readlines()
            if len(used_words_list) == 0:
                print("No one words in file")
            i = 0
            for word in used_words_list:
                print(word.strip(), end=" ")
                if i == 10:
                    print()
                i += 1
            print("\n")

    print("Press Enter to returm in main menu")
    input()
    return


def print_start_screen():
    """Draws main menu logo"""
    os.system("clear")
    print()
    print("    []   []    []    []  []   /[]\    []    []    []    []  []")
    print("    []   []   [  ]   []\ []  []   ]   []\  /[]   [  ]   []\\ []")
    print("    []///[]  [====]  [] \\[]  [] ~\    [] \/ []  [====]  [] \\[]")
    print("    []   []  [    ]  []  []   \[]/    []    []  [    ]  []  []" )
    print()


def is_letter(letter: str) -> bool:
    """This function check letter argument is a single English letter"""
    reg_exp = re.compile("[A-Za-z]")
    res = reg_exp.match(letter)
    if len(letter) == 1 and res:
        return True
    else:
        return False


LIFES_INIT = 10  # initial count of tries

while True:
    print_start_screen()
    print("'1' - to start game")
    print("'2' - to see words used in game")
    print("'3' - to exit")
    menu_choice = int(input())
    if menu_choice == 1:
        lifes = LIFES_INIT
        word_in_game_str = pick_word()   # hidden word
        used_letters_list = []           # list of used letters
        guessed_letters_list = ["_"] * len(word_in_game_str)  # hidden word presentation
        while True:
            draw_hangman(lifes)
            if lifes == 0:  # check loose condition and exit
                print("You lose...")
                with open("used_words.txt", "a") as f:
                    f.write(word_in_game_str + "\n")
                    f.close()
                print(f"The word is: {word_in_game_str}")
                input("Press Enter to return to the main menu")
                break

            print(" ".join(guessed_letters_list))

            if "_" not in guessed_letters_list:  # check win condition
                print("You win!")
                with open("used_words.txt", "a") as f:
                    f.write(word_in_game_str + "\n")
                    f.close()
                input("Press enter to return to the main menu")
                break
            print(f"You have: {lifes} tries. Not matched letters: {' '.join(used_letters_list) }")
            guess_letter = input("enter a letter\n")
            if is_letter(guess_letter) and guess_letter not in used_letters_list:
                temp_list = find_all(word_in_game_str, guess_letter)[:]
                if len(temp_list) > 0:
                    for i in temp_list:
                        guessed_letters_list[i] = guess_letter
                else:
                    lifes -= 1
                    used_letters_list.append(guess_letter)

    elif menu_choice == 2:
        show_used_words()
    elif menu_choice == 3:
        exit(0)





