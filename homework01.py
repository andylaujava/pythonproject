import math
radius=eval(input("請輸入圓柱體的半徑(公分):"))
height=eval(input("請輸入圓柱體的高(公分):"))
volume=math.pi*radius**2*height

print(f"圓柱體的體積:{volume:.2f}立方公分")