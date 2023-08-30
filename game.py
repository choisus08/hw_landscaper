# Store game data in a dictionary
game_data = {
    "money": 0,
    "quit": False
}

# Using the rusty scissors, you can spend the day cutting lawns and make $5. You can do this as much as you want.
def use_scissors():
    while (True):
        user_input = int(input(""" 
                        Would you like to use the scissors to work and earn $5?
                        [1] Yes! My teeth hurt!
                        [2] No, I'll keep using my chompers 
                        """))
        if (user_input == 1):
            game_data["money"] += 5
            print(f"You now have ${game_data['money']}")

            # At any point, if you are currently using rusty scissors, you can buy an old-timey push lawnmower for $25. You can do this once, assuming you have enough money.
            if (game_data["money"] >= 25):
                user_input = int(input("""
                                Would you like to purchase an old-timey push lawnmower for $25?
                                [1] Yes! My fingers can use a break!
                                [2] No, I'll still use the scissors and save
                                """))

                if (user_input == 1):
                    game_data["money"] -= 25
                    print(f"You now have ${game_data['money']}")
                    use_lawnmower()


                    # if user has no money, start over
                    if (game_data["money"] == 0):
                        use_teeth()
                        
                if (user_input == 2):
                    continue            

        if (user_input == 2):
            use_teeth()


# Using the old-timey push lawnmower, you can spend the day cutting lawns and make $50. You can do this as much as you want.
def use_lawnmower():
    while (True):
        user_input = int(input("""  
                        Would you like to use the old-timey push lawnmower to cut lawns and earn $50?
                        [1] Yes!
                        [2] No, thank you
                        """))
        
        if (user_input == 1):
            game_data["money"] += 50
            print(f"You now have ${game_data['money']}")

        if (user_input == 2):
            use_scissors()
        

# You are starting a landscaping business, but all you have are your teeth.
# Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want.
def use_teeth(): 
    while (True):
        user_input = int(input("""
                        Would you like to cut lawns with your teeth today and earn $1?
                        [1] Yes!
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
                    use_scissors()
         
                if (user_input == 2):
                    continue


        if (user_input == 2):
            game_data["quit"] = True

        if (game_data["quit"] == True):
         print("You quit the game")
         break
    
use_teeth()