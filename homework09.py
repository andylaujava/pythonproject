import random

name=str(input("請輸入學生姓名:"))
students = []
for i in range(1):
    scores = []
    for j in range(5):
        scores.append(random.randint(50,100))
    students.append(scores)
print(f"{name}的成績如下:")
print("國文\t英文\t數學\t自然\t社會")
for score in students:
    for item in score:
        print(item,end="\t")
    print()

