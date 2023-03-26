

if sbp<120 and dbp<80:
 suggestion="正常"

if 120<=sbp<=129 and dbp<80:
 suggestion="高血壓升高"

if 130<=sbp<=139 or 80<=dbp<=89:
 suggestion="高血壓一期"

if sbp>=140 or dbp>=90:
 suggestion="高血壓二期"

if sbp>=130 and dbp<80:
 suggestion="單純收縮期高血壓"
print(suggestion)

