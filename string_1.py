# -*- coding:utf-8 -*-

str2 = "abc123456"

# 从字符串中取出指定位置的字符
print(str2[2])

# 字符串切片
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45


str1 = "hello,wordl!"
# 计算字符串长度
print(len(str1))

# 获得字符串每个单词首字母大写拷贝
print(str1.title())

# 获得字符串变大后的拷贝
print(str1.upper())

# 字符串中查找子串所在位置,找不到时返回-1
print(str1.find('or'))

# 检查字符串是否由数字构成
print(str2.isdigit())

# 检查字符串是否以字母构成
print(str2.isalpha())

# 检查字符串是否以数字和字母构成
print(str2.isalnum())

str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())