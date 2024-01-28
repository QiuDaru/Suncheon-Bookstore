import random
import time

print("歡迎來玩棒打老虎雞吃蟲")

def cmp():
    x = random.randint(1, 4)
    while True:
        user_input = input("------\n請輸入您選擇的角色\n1.棒\n2.老虎\n3.雞\n4.蟲\n輸入編號:")
        if user_input.isdigit() and int(user_input) in (1, 2, 3, 4):
            y = int(user_input)
            global w1,w2
            w1 = "玩家"
            w2 = "電腦"
            test(x, y)
            break
        else:
            print("\n\n\n請輸入有效的數字！")

def test(x, y):
    global w1
    global w2
    win = [(1, 2), (2, 3), (3, 4), (4, 1)]
    if (y, x) in win:
        print(f"\n{w1}贏")
    elif (x, y) in win:
        print(f"\n{w2}贏")
    else:
        print("\n平手")
    time.sleep(3)

def user_play():
    while True:
        user_input1 = input("------------\n玩家一   請選擇你的角色\n請輸入您選擇的角色\n1.棒\n2.老虎\n3.雞\n4.蟲\n輸入編號:")
        user_input2 = input("\n\n\n\n\n\n\n\n\n\n\n------------\n玩家二   請選擇你的角色\n請輸入您選擇的角色\n1.棒\n2.老虎\n3.雞\n4.蟲\n輸入編號:")
        if user_input1.isdigit() and user_input2.isdigit() and int(user_input1) in (1, 2, 3, 4) and int(user_input2) in (1, 2, 3, 4):
            x = int(user_input1)
            y = int(user_input2)
            global w1,w2
            w1 = "玩家二"
            w2 = "玩家一"
            test(x, y)
           
            break
        else:
            print("\n\n\n請輸入有效的數字！")

while True:
    play = input("\n\n\n\n\n\n\n\n請選擇遊戲模式\n 1. 玩家vs電腦\n 2. 玩家vs玩家\n3.退出遊戲\n輸入您的選擇(數字):")

    if play == "1":
        cmp()

    if play == "2":
        user_play()

    if play == "3":
        break
print("遊戲結束")