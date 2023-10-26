num = int(input("Digite um numero: "))

primo = True

if num <= 1:
    primo = False
else :
    for divisor in range(2, num):
        if num % divisor == 0:
            primo = False
            break
if primo:
    print(f" O número {num} é primo")
else :
    print(f" O número {num} não é primo")