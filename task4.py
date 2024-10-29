# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
mas1=[]
mas2=[]
def Nod(n,k):
    for i in range(1,min(n,k)):
        if min(n,k)%i==0:
            mas1.append(i)    
    for j in mas1:
        if max(n,k)%j==0:
               mas2.append(j)
    print(max(mas2))
n=int(input())
k=int(input())
Nod(n,k)
