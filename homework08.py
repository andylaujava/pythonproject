import random

lot=set()
inputvalue=int(input("請輸入大樂透電腦選號組數:"))
for lot in range(inputvalue):
        lot=random.randint(1,49)
        pack=[]
        for _ in range(7):
                pack.append(random.randint(1,49))
        
        print(f"您的大樂透電腦選號為:{pack},特別號:{pack[-1]}")       