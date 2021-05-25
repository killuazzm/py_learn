num = [1,3,4,5]
print(num)
len(num)
print(num[0])

# 追加元素至list末尾
num.append(6)
# 插入元素
num.insert(1,2)
# 删除末尾元素
num.pop()
# 删除指定位置元素
num.pop(1)

# 计算列表长度
print(len(num))

# 使用循环遍历列表元素
for index in range(len(num)):
    print(num[index])
for elem in num:
    print(elem)

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(num):
    print(index, elem)

# 添加元素
num.append(6)
num.insert(1,2)

list1 = [1,2]
list2 = [3,4]
# 合并列表
list3 = list1 + list2
list1.extend(list2)
print(list3)
print(list1)

# 判断元素是否在列表中，是就删除
if 1 in list1:
    list1.remove(1)
if 0 in list1:
    list1.remove(0)
print(list1)

# 清空列表元素
list1.clear()
print(list1)

# 切片操作
list4 = [1,2,3,4,5]
print(list4[1:4])
print(list4[-3:-1])
print(list4[::-1])

str1 = ['orange','apple','zoo','internet','blueberry']
# 对列表的排序
str2 = sorted(str1) # sorted函数返回列表排序后的拷贝，不会修改传入的列表
str3 = sorted(str1,key=len) # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
print(str2)
print(str3)