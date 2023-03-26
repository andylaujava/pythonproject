sbp=int(input("請輸入收縮壓:"))
dbp=int(input("請輸入舒張壓:"))

if sbp>=140 or dbp>=90:
    suggestion="高血壓二期"
elif sbp>=130 or 80<=dbp<=89:
    suggestion="高血壓一期"
elif sbp>=120 and dbp<80:
    suggestion+"血壓升高"
elif dbp<80:
    suggestion="正常"

if sbp>=130 and dbp<80:
    suggestion="單純收縮期\n高血壓"
print(suggestion)