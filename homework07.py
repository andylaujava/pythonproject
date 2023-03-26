sum=0
num=0

while (True):
        input_value=int(input(f"請輸入第{num+1}個整數,輸入負數，結束程式:"))
        if (input_value==-1):
                break
                print("程式結束")
        if (input_value%2==0):        
                num+=1
                sum += input_value
        elif(input_value%2>0):
                continue
        
        
print(f"您輸入的偶數加總為:{sum}")       