# Viet mot script Python de sap xep (tan dan va giam dan) mot dictionary theo gia tri

import operator
my_dict = {
    'a':3, 
    'b':1, 
    'c':2,
    'd':0,
    'e':7,
    'f':5,
    'g':6,
    'h':9,
    'i':8,
    'k':5
}
print(my_dict)

sorted_my_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=False))
print(sorted_my_dict)

# Viet mot script Python de noi cac tu dien de tao thanh mot tu dien moi

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}
for i in (dic1, dic2, dic3):
    dic4.update(i)
print(dic4)

# Viet mot script Python de kiem tra mot tu khoa co ton tai trong dict khong ?

dic = {'dang':28, 'tuan':8, 'minh':2002}

if 'dang' in dic:
    print(True)
else:
    print(False)