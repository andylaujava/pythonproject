ages=int(input("請輸入年齡:"))
if ages>=18:
    print("限制級:18歲或以上皆可觀賞")
elif 13<=ages<=17:
    print("輔導級:13(含)~17歲以上皆可欣賞。")
elif ages<=12:
    print("普遍級:12歲(含)以下皆可觀賞")

