# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
def is_valid_triangle(side1, side2, side3):
    if (side1+side2)>side3 and (side1+side3)>side2 and (side3+side2)>side1:
        print("True")
    else:
        print("False")
side1=int(input())
side2=int(input())
side3=int(input())
is_valid_triangle(side1, side2, side3)
