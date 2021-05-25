# -*- coding:utf-8 -*-

# 实现计算求最大公约数和最小公倍数的函数


def gcd(x,y):
    # () if () else () 是一个三目运算符
    (x,y) = (y,x) if x > y else (x,y)
    for factor in range(x,0,-1)
