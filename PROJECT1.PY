name=input("Hey type your name here to start the game: ")
print("Hello "+ name +" welcome to My game!")

should_we_play=input("do you want to play:").lower()

if should_we_play == "y" or "yes":
    print("You're gonna play")

    direction=input("In which direction you need to go (left/right): ").lower()
    if direction == "left":
        print("You can find the lake")
    elif direction == "right":
        print("You can find the Maze")
    else:
        print("You can't able to continue playing")
    
    weapon = input("select weapon:(axe/pistol): ").lower()
    if weapon == "axe":
        print("you can able to continue with left side")
    elif weapon == "pistol":
        print("you can able to continue with right side")
    else:
        print("You can't able to continue to fight the enemy")
else:
    print("if you did not enter y or yes, you can't able to continue playing")