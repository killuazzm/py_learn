# 创建一个集合
set1 = {1,2,3,3,3,4}
print(set1)
print('length = ',len(set1))

# 创建集合的构造器语法
set2 = set(range(1,10))
print(set2)

# 创建集合的推导式语法
set3 = {num for num in range(1,100) if num % 3 == 0 or num % 5 == 0}
print(set3)

# 常用操作
set1.add(5)
set1.update([6,7])
set1.discard(1)
if 4 in set1:
    set1.remove(4)
print(set1)
print(set1.pop())


seta = {1,2,3,4}
setb = {2,3,4,5}
# 集合运算
print(seta & setb)# 交集
# print(set1.intersection(set2))
print(seta | setb)# 并集
# print(set1.union(set2))
print(seta - setb)# 差集
# print(set1.difference(set2))
print(seta ^ setb)# 对称差
# print(set1.symmetric_difference(set2))

# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
