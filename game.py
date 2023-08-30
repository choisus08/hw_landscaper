# Store game data in a dictionary
game_data = {
    "money": 0,
    "quit": False
}

# You are starting a landscaping business, but all you have are your teeth.
# Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want.
def use_teeth(): 
    while (True):
        user_input = int(input("""
                        Would you like to cut lawns with your teeth today?
                        [1] Yes, earn $1
                        [2] Not today
                        """))
                        
        if (user_input == 1):
            game_data["money"] += 1
            print(f"You now have ${game_data['money']}")

        if (user_input == 2):
            game_data["quit"] = True

        if (game_data["quit"] == True):
         print("You quit the game")
         break
    
use_teeth()