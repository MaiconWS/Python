import random

num_secret = random.randint(1,10)

print("Bem vinda ao jogo de adivininhação !")
print("Tente adivinhar o numero secreto entre 1 e 10.")

while True:
    palpite = int(input("Digite seu palpete: "))

    if palpite == num_secret:
        print(f"Parabens! Você acertou o numero {num_secret}.")
        break
    elif palpite < num_secret:
        print("Tente um numero maior.")
    else:
        print("Tente um numero menor.")