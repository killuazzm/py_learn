# -*- coding:utf-8 -*-

from random import randint

# 本程序实现快速摇人

stu = ["杨智豪","李超","闫子尧","常海栋",
"薛伟","蒲茜豪","冯东阳","胡方钲","林梦杰","马名扬"
,"潘自强","张梓明","魏浩","张博涛","王兴哲","高路通"
,"赵云龙","王晨辉","赵博爱","贾子龙","郭自长","唐彬斌"
,"赵自成","刘超民","毛玉富","赵辉辉","董喆","冯蕾","陈苑以"]

stu_xuan = []

def random_stu(stu_num,need_num):
    for i in range(0,need_num):
        n = stu.pop(randint(1,stu_num-i))
        stu_xuan.append(n)

def del_stu(stu_name):
    stu.remove(stu_name)
    print("已从候选列表中删除"+stu_name)



if __name__  == "__main__":
    num1 = int(input('需要几人：'))
    is_del = int(input('需要删除几人'))
    for i in range(is_del):
        stu_name = input('输入删除名称:')
        del_stu(stu_name)
    random_stu(29,num1)
    print(stu_xuan)