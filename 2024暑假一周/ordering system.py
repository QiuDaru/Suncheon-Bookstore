#menu_items = ["pizza","steak","pasta"]
#menu_items_price = [11,30,15]
ingredients = {"slice of bread":10,"cheese":10,"lettuce":5, "tomato":10, "ham":15, "mayo":5, "peanut butter":5, "strawberry jam": 6, "chocolate syrup":6, "honey":6, "bean sprout":10, "beef":20, "egg":12, "bell pepper":10, "red beans":10, "mochi":30, "strawberries":}

user_choice = list(map(str,input().split()))
spend = 0
for i in user_choice:
        spend += menu_items[i]
print(spend)






#for i in user_choice:
 #   if i in menu_items:
  #      spend += menu_items_price[menu_items.index(i)-1]
#print(spend)


    