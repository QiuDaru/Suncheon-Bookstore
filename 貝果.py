import random

guess = 0
Answer = random.sample(range(1,10), 3)
print("請猜100到1000的數，你有十次機會\n提示有以下幾種\n1.猜對一個字,順序錯\n2.猜對一個字,順序對\n3.沒猜到數字")

while True:
    user = input("請輸入一個三位數:")
    try:
        text = [int(i) for i in user]
        print(Answer)
        if len(text) != 3:
            print("請輸入三位數！")
            
            continue
        if user == Answer:
            print("你贏了")
            print(guess)
            break
        else:
            for i in range(3):
                
                if Answer[i] == text[i]:
                    print("猜對一個數字位置對了")
                    break
            
            
        print("都沒對")  
        guess = guess+1
    except ValueError:
        print("請輸入數字")
        