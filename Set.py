my_set = {1, 2, 'a', 'b', 3}
print(my_set)

for i in my_set:
    print(i)

my_set.add('c')
print(my_set)

my_set.remove(1)
print(my_set)

# Giao cua hai set
setX = {1, 2, 3, 4}
setY = {2, 3, 5, 7}
setZ = setX & setY
print(setZ)

# Loai bo cac phan tu cua set1 giong voi set2
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
s1 = set1.difference(set2)
print(s1)

# Hop hai set
print(s1)
set3 = set()
for i in (set1, set2):
    set3.update(i)
print(set3)