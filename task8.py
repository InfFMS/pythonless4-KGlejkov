# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
def f(n):
    if n==1:
        return " "
    else:
        for i in range(2, int(n**0.5)+2):
            if n%i==0:
                n//=i
                return str(i)+"*"+str(f(n))
                break
n=int(input())
print(f(n)[:-2])

