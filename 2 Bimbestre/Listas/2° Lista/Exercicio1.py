from datetime import date

nascimento = int(input("Digite o ano de seu nascimento => "))

ano = date.today().year

idade = ano - nascimento

print(idade)