for i in range(1,10):
    for i1 in range(1,10):
        print(i*i1)


#=========================================

x = 0
while True :
    if x == 20:
        break
    x+=1
    print(x)
    while True:
        x+=1
        print("1")
        if x == 20:
            break