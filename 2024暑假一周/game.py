print("you are a hamster lost in the forest")
user_input = input("Please choose your action (enter a number) \n 1. Eat \n 2. Run \n :").s
food = 1
hunger_value = 2
def eatfood():
    print("now you are full")
    food -=1
    hunger_value = 10
    if food == 0:
        print("but you don't have any food")

if user_input == "1":
    eatfood() 
    