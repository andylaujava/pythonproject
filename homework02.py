score=int(input("請輸入成績(0-100):"))
if score>=90:
    grade="優等"
else:
    if score>=80:
        grade="甲"
    else:
        if score>=70:
            grade="乙"
        elif score>=60:
            grade="丙"
        else:
            grade="丁"
print(grade)
        