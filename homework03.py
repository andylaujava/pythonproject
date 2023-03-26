money=int(input("請輸入購買金額:"))
if money>=100000:
    paymoney=money*.8
elif money>=50000:
    paymoney=money*85
elif money>=30000:
    paymoney=money*.9
elif money>=10000:
    paymoney=money*.95
else:
    paymoney=money
print("實付金額是:",paymoney,"元")


