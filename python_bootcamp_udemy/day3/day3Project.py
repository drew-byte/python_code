print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
input1 = input("Move Left or Right: ").lower()
if input1 == "left":
    input2 = input("Swim or Wait: ").lower()
    if input2 == "swim":
        input3 = input("----------\nWhich Door?\nRed    [1]\nBlue   [2]\nYellow [3]\n----------\nAnswer: ")
        if input3 == "1":
            print("Burned by fire.\nGame Over.")
        elif input3 == "2":
            print("Eaten by beasts.\nGame Over.")
        elif input3 == "3":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")
