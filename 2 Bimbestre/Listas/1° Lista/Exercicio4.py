numero1 = float(input("Digite o 1° numero... "))
numero2 = float(input("Digite 0 2° numero..."))

if numero2 == 0:
    print("O segundo numero não pode ser zero")

else:
    if numero1 % numero2 == 0:
        print(f"{numero1} é divisivel por {numero2}")
    else:
        print(f"{numero1} não é divisivel por {numero2}")