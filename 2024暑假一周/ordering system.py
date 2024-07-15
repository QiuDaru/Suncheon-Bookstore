#menu_items = ["pizza","steak","pasta"]
#menu_items_price = [11,30,15]
ingredients = {"slice of bread":10,"cheese":10,"lettuce":5, "tomato":10, "ham":15, "mayo":5, "peanut butter":5, "strawberry jam": 6, "chocolate syrup":6, "honey":6, "bean sprout":10, "beef":20, "egg":12, "bell pepper":10, "red beans":10, "mochi":30, "strawberries":20}
spend = 0
user_choice = input("what do you need ? choose one number\n 1.print menu \n 2.order your sandwich \n 3.Enter a price and I'll make you a sandwich : ")

def choice1(ingredients1):
        for ingredient, price in ingredients1.items():
                print(f"{ingredient}: ${price}")





def choice2(ingredients):
        user_choice=list(map(str,input("order your sandwich : ").split()))
        spend = 0
        for i in user_choice:
                spend += ingredients[i]
        print(spend)

def choice3(ingredients,cost):
        for i in range(ingredients.values()):
                for i1 in range(ingredients.values()):
                        for i2 in range(3):
                                if i+i1 == cost:
                                        



        


if user_choice == "1":
        choice1(ingredients)
if user_choice == "2":
        choice2(ingredients)
if user_choice == "3":
        cost = input("cost : ")
        choice3(ingredients,cost)


#for i in user_choice:
 #       spend += ingredients[i]



#print(spend)






#for i in user_choice:
 #   if i in menu_items:
  #      spend += menu_items_price[menu_items.index(i)-1]
#print(spend)


    