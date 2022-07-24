# Escribe una función que calcule el área de un triángulo, recibiendo la altura

altura = int(input("Ingrese altura: "))
base = int(input("ingrese base: "))
def areaTriangulo ():
        area = int((altura*base)/2)
        print("el area de un triangulo es : ", area)
print(areaTriangulo())


# y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.


from math import pi

def area_circulo(radio):

    radio = float(radio)
    area = pi * radio ** 2
    return format(area, ".1f")

radio = input("Ingrese el radio del circulo: ")

tota_area = area_circulo(radio)

print("El area del circulo es:", tota_area)
