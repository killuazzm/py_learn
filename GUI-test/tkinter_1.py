# -*- coding:utf-8 -*-
from hashlib import sha3_224
import tkinter
from tkinter.constants import LEFT, NW, RIGHT, S, TOP
from random import randint

stu = ["杨智豪","李超","闫子尧","常海栋",
"薛伟","蒲茜豪","冯东阳","胡方钲","林梦杰","马名扬"
,"潘自强","张梓明","魏浩","张博涛","王兴哲","高路通"
,"赵云龙","王晨辉","赵博爱","贾子龙","郭自长","唐彬斌"
,"赵自成","刘超民","毛玉富","赵辉辉","董喆","冯蕾","陈苑以"]

stu_xuan = []
stu_del = []
# 选人
def random_stu(stu_num,need_num):
    for i in range(0,need_num):
        n = stu.pop(randint(1,stu_num-i))
        stu_xuan.append(n)

# 删人
def del_stu(stu_name):
    stu.remove(stu_name)
    print("已从候选列表中删除"+stu_name)
    S1 ='已从候选列表中删除' + str(stu_name)
    stu_del.append(S1)

# 得到表格中数值并选人
def get_num():
    a = button2.get()
    random_stu(29,a)

    


# GUI界面
top = tkinter.Tk()
# 界面框架
# jm = tkinter.Frame(top,height=600,width=800)
text1 = tkinter.Label(top,anchor=NW,text='需求人数')
text1.pack()

button2 = tkinter.Entry(top,bd=5)
button2.pack()

button1 = tkinter.Button(top,text='确认',command=get_num)
button1.pack()


text2 = tkinter.Label(top,text='删除：')
text2.pack()

# 删掉不选的名字
button_del = tkinter.Button(top,text='删除',command=del_stu)
button_del.pack()

button_delnum = tkinter.Button(top,bd=5)
button_delnum.pack()

button_delname = tkinter.Text(top,stu_del)


# 进入消息循环
top.mainloop()