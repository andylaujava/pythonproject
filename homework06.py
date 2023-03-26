import math
height=float(input("請輸入身高，單位為(公分):"))
weight=float(input("請輸入體重，單位為(公斤):"))
bmi=weight/(height/100)**2
if bmi<18.5:
    print(f"您的bmi:{bmi:.2f}\n體重太輕")
elif bmi>30:
     print(f"您的bmi:{bmi:.2f}\n體重肥胖")
elif 18.5<=bmi<=25:
      print(f"您的bmi:{bmi:.2f}\n體重正常")
elif 25<=bmi<=30:
     print(f"您的bmi:{bmi:.2f}\nwu體重過重")
