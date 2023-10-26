lado1 = float(input("Informe o comprimento do 1° lado => "))
lado2 = float(input("Informe o comprimento do 2° lado => "))
lado3 = float(input("Informe o comprimento do 3° lado => "))

triangulo = (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

if triangulo :
    print("Os lados podem formar um triangulo")
else:
    print("Os lados não podem formar um triangulo")