import math


a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))


delta = max(b**2 - 4*a*c, 0)


x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print(f"As raízes são: {x1} e {x2}")



ano = int(input("Digite um ano: "))


is_bissexto = (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0))

print(is_bissexto) 

