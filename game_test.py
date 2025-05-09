def start_game():
    print("You wake up in a dark forest. Do you go LEFT or RIGHT?")
    choice = input("> ").lower()

    if choice == "left":
        print("You find a sword! Now fight the dragon.")
    elif choice == "right":
        print("A trapdoor opens... Game Over!")
    else:
        print("Invalid choice. Try again.")
        start_game()

start_game()