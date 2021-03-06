# 生成式与生成器
f = [x for x in range(1,10)]
print(f)

f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

f = [x ** 2 for x in range(1,10)]
print(f.__sizeof__)  # 查看对象占用内存的字节数

# 下面的代码创建一个生成式
f1 = (x ** 2 for x in range(1,10))
print(f.__sizeof__)
print(f)
for val in f:
    print(val)

# 通过yield关键字将函数改造成生成器函数
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    yield a