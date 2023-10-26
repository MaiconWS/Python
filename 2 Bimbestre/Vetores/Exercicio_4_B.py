Musicas = ['Strangers','Bags','Fall into u','I Found A Reason','You re So God', "Dissolve in The Rain"]

Verificacao = input("Qual musica deseja procurar ?") in Musicas

if Verificacao:
    print("Está na sua lista de musicas favorita!")
else:
    print("Não foi encontrado em sua lista de musicas favorita!")

    Musicas.append(input("Inseria sua musica: "))

    Verificacao = input("Qual musica deseja procurar ?") in Musicas

    if Verificacao:
        print("Está na sua lista de musicas favorita!")
    else:
        print("Não foi encontrado em sua lista de musicas favorita!")