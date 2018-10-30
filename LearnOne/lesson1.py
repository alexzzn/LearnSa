# 阶乘递归
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# 斐波那契函数
# 简单的递归
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# 简单的循环
def fibLoop(n):
    f1 = f2 = 1
    for i in range(0, n):
        f1, f2 = f2, f1 + f2
    return f2


# print(fib(100))
# print(fibLoop(100))
# print(factorial(3))