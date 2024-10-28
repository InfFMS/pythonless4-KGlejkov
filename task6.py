# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3
mas1=[]
mas2=[]
def f(n,k):
    for i in range(1,min(n,k)+1):
        if min(n,k)%i==0:
            mas1.append(i)    
    for j in mas1:
        if max(n,k)%j==0:
               mas2.append(j)
    print(n//max(mas2),k//max(mas2))
n=int(input())
k=int(input())
f(n,k)
