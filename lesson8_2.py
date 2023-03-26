#直角三角形
import math

def hypotenuse(side,otherside):
    return math.sqrt(side**2+otherside**2)
s=eval(input("請輸入一邊:"))
os=eval(input("請輸入另外一邊:"))

hypotenuse(s,os)
print(hypotenuse)
