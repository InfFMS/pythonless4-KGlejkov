# Напишите процедуру, которая принимает параметр – натуральное число N –
# и выводит на экран треугольник из * с катетами равными N.
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
def f(n):
    for i in range (n):
        print('*' * (i+1))
n=int(input())
f(n)

