num = int(input("Digite um numero: "))

fatorial = 1

for i in range (1, num+1):
    fatorial *= i
print(f"O fatorial de {num} é => {fatorial}")