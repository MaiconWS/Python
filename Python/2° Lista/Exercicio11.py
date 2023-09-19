usuario = input("Login: ")

if usuario == "maicon":
    senha = input("Senha: ")
    if senha == "teste":
        print("Login concluido")
    else:
        print("Senha incorreta")
else:
    print("Login incorreto")
