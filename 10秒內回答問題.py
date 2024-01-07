import time#time
seconds1 = time.time()
print("若想要有好康的請在10秒內回答傑哥問題")
input('傑哥:我叫阿傑,他們都叫我傑哥,你叫甚麼?:') 
seconds2 = time.time()
if seconds2-seconds1 >= 120:
    print("傑哥:哼!時間超過了不給你好康的了")
else:
    print('傑哥:來給你好康的')
