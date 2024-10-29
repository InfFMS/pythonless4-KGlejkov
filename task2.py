# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять
mas1=["","","двадцать","тридцать","сорок","пятьдесят","шестьдесят","семдесят","восемьдесят","девяносто"]
mas2=["","один","два","три","четыре","пять","шесть","семь","восемь","девять"]
mas3=["десять","однадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"]
def f(n):
    if n>=20:
        print(mas1[n//10],mas2[n%10])
    elif 9>=n>=1:
        print(mas2[n])
    elif 19>=n>=10:
        print(mas2[n%10])
    else:
        print("ноль")  
n=int(input())
f(n)
