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

            # At any point, if you are currently using your teeth, you can buy a pair of rusty scissors for $5. You can do this once, assuming you have enough money.
            if (game_data["money"] >= 5):
                user_input = int(input("""
                                Would you like to purchase a pair of rusty scissors for $5?
                                [1] Yes
                                [2] Not right now
                                """))
                if (user_input == 1):
                    game_data["money"] -= 5
                    print(f"You now have ${game_data['money']}")

                if (user_input == 2):
                    continue



        if (user_input == 2):
            game_data["quit"] = True

        if (game_data["quit"] == True):
         print("You quit the game")
         break
    
use_teeth()