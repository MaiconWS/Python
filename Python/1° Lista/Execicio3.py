numero1 = int(input("Digite o 1° numero... "))
numero2 = int(input("Digite 0 2° numero..."))
numero3 = int(input("Digite 0 3° numero..."))

if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1

elif numero2>= numero1 and numero2 >= numero3:
    maior = numero2

else :
    maior = numero3

print(f"Entre o numero {numero1}, {numero2} e {numero3} o maior é {maior}")