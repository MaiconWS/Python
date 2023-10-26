lado1 = float(input("Informe o comprimento do 1° lado => "))
lado2 = float(input("Informe o comprimento do 2° lado => "))
lado3 = float(input("Informe o comprimento do 3° lado => "))

if lado1 == lado2 == lado3:
    print("É um triangulo equilatero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("É um trangulo isósceles.")
else:
    print("É um triangulo escaleno.")