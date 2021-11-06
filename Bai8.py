"""
try: #Khoi lenh co the phat sinh loi
    ...
except: #Khoi lenh duoc thuc thi khi loi xay ra
    ...
"""

# VD1
try:
    a = int(input())
    b = int(input())
    print("a + b =", a + b)
except:
    print("Dau vao khong hop le!")

# VD2
try:
    x, y, z = map(float, input().split())
    print(x + y + z)
except:
    print("Dinh dang dau vao khong hop le!")

# VD3
arr = [2, 5, 6, 'a']
for i in arr:
    try:
        print(i / 2)
    except:
        print("Error!")
