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
                    use_old_lawnmower()

                    # if user has no money, start over
                    if (game_data["money"] == 0):
                        use_teeth()
                        
                if (user_input == 2):
                    continue            

        if (user_input == 2):
            use_teeth()


# Using the old-timey push lawnmower, you can spend the day cutting lawns and make $50. You can do this as much as you want.
def use_old_lawnmower():
    while (True):
        user_input = int(input("""  
                        Would you like to use the old-timey push lawnmower to cut lawns and earn $50?
                        [1] Yes!
                        [2] No, thank you
                        """))
        
        if (user_input == 1):
            game_data["money"] += 50
            print(f"You now have ${game_data['money']}")

            # At any point, if you are currently using the old-timey push lawnmower, you can buy a fancy battery-powered lawnmower for $250. You can do this once, assuming you have enough money.
            if (game_data["money"] >= 250):
                user_input = int(input("""
                                This old lawnmower is not efficient, how about upgrading to a fancy battery-powered one for $250?
                                [1] Yes! That'll make the work so much easier to do!
                                [2] I'll pass and save more for now
                                """))
               
                if (user_input == 1):
                    game_data["money"] -= 250
                    print(f"You now have ${game_data['money']}")
                    use_battery_lawnmower()

                if (user_input == 2):
                    continue

        if (user_input == 2):
            use_scissors()


# Using the the fancy battery-powered lawnmower, you can spend the day cutting lawns and make $100. You can do this as much as you want.
def use_battery_lawnmower():
    while (True):
        user_input = int(input("""
                        Would you like to cut lawns using the fancy battery-powered lawnmower to earn $100? 
                        [1] Yes, whatever will get the job done better & quicker!
                        [2] No, I'll use it another day
                        """))
        if (user_input == 1):
            game_data["money"] += 100
            print(f"You now have ${game_data['money']}")

                # At any point, if you are currently using the fancy battery-powered lawnmower, you can hire a team of starving students for $500. You can do this once, assuming you have enough money.
            if (game_data["money"] == 500):
                user_input = int(input(""" 
                                Do you want to hire a team of starving students for $500?
                                [1] Yes! I'll be glad to hire them!
                                [2] Sorry, I'll pass for now
                                """))
                if (user_input == 1):
                    game_data["money"] -= 500
                    print(f"You now have ${game_data['money']}")
                    use_students()

                if (user_input == 2):
                    continue

        if (user_input == 2):
            use_old_lawnmower()


# Using the the team of starving students, you can spend the day cutting lawns and make $250. You can do this as much as you want.
def use_students():
    while (True):
        user_input = int(input(""" 
                        Do you want your team of students to spend the day cutting lawns and earn $250?
                        [1] Yes!
                        [2] Not today
                        """))
        
        if (user_input == 1):
            game_data["money"] += 250
            print(f"You now have ${game_data['money']}")
        
        if (user_input == 2):
            continue

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

                    # if user has no money, start over
                    if (game_data["money"] == 0):
                        use_teeth()
         
                if (user_input == 2):
                    continue


        if (user_input == 2):
            game_data["quit"] = True

        if (game_data["quit"] == True):
         print("You quit the game")
         break
    
use_teeth()