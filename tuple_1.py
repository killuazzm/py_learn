# 元组是不可变的
num1 = (0,)
num2 = (1,2,3)

# 元组中的列表是可以修改的，这并不意味着元组可变
list1 = [1,2,3]
num3 = (list1,4,5)
print(num3)
list1[0] = 0
print(num3)