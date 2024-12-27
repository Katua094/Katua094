import random

comp_choice = random.randint(0, 100)

while True:
    choice = int(input("Take a guess, put in a number between 0 and 100, or 900 to quit: "))

    if choice == comp_choice:
        print("You win my guy \n")

        play_again = input("Do you want to play again? (yes) or (no) ").lower()
        if play_again == "yes":
            comp_choice = random.randint(0, 100)
            continue
        elif play_again == "no":
            print("Byee !")
            break

    elif choice > comp_choice and choice < 100:
        print("too high \n")
    elif choice < comp_choice and choice < 100:
        print("too low my guy\n")
    elif choice == 900:
        print("Byee!!")
        break
