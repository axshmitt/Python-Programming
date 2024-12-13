import random

def play_game(player_name):
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
    attempts = 5
    games_won = 0
    games_lost = 0

    while True:
        machine_color = random.choice(colors)
        attempts_left = attempts
        game_won = False

        print("\nGuess the color from:", ", ".join(colors))

        while attempts_left > 0:
            user_color = input("Please enter the color: ").lower()

            if user_color not in colors:
                print("Invalid color. Please choose from the list.")
                continue

            if user_color == machine_color:
                print("You won the game!")
                print(f"Number of attempts: {attempts - attempts_left + 1}")
                game_won = True
                games_won += 1
                break
            else:
                attempts_left -= 1
                print("Your guess was wrong, please try again.")
                print(f"Number of attempts left: {attempts_left:02}")

        if not game_won:
            print(f"You lost! The correct color was: {machine_color}")
            games_lost += 1

        print("\n1> See score board\n2> Play again\n3> Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print(f"\n--- Score Board ---\nNumber of games won: {games_won}\nNumber of games lost: {games_lost}\nName of the player: {player_name}\n")
        elif choice == '3':
            print("Thank you for playing!")
            break

print("Welcome to the color game>>>")
player_name = input("Please enter the name for score board: ")

while True:
    print("\n1> Start Game\n2> Exit")
    main_choice = input("Enter your choice: ")
    if main_choice == '1':
        play_game(player_name)
    elif main_choice == '2':
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice, please enter 1 or 2.")
