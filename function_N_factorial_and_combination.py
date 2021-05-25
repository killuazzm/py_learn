# -*- coding:utf-8 -*-

def fac(num):
    ans = 1
    for i in range(1,num+1):
        ans *= i
    return ans


def comp(n,m):
    fm = fac(n) * fac(m-n)
    return fac(m)/fm

cm = int(input('m = '))
cn = int(input('n = '))

print(comp(cn,cm))

# python的math模块中包含factorial函数，其实现了阶乘运算