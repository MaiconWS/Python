Livros = ['Determinada','Fallen','Tormenta','Divergente']

Verificacao = input("Qual livro deseja procurar ?") in Livros

if Verificacao:
    print("Está na sua lista de livros favorita!")
else:
    print("Não foi encontrado em sua lista de livros favorita!")

    Livros.append(input("Inseria sua livro: "))

    Verificacao = input("Qual livro deseja procurar ?") in Livros

    if Verificacao:
        print("Está na sua lista de livros favorita!")
    else:
        print("Não foi encontrado em sua lista de livros favorita!")