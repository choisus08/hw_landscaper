# Start game
user_input = input("Give any whole number to start the game")
print(2 + int(user_input))

# Store game data in a dictionary
game_data = {
    "point": 0,
    "quit": False
}

while (True):
    user_input = int(input("""
                     Do you want to cut lawns with your teeth today?
                     [1] Yes, make $1
                     [2] No, quit the game  
                    """))
    if (user_input == 1):
        game_data["point"] += 1
        print(f"You now have ${game_data['point']}")

    if (user_input == 2):
        game_data["quit"] = True
    
