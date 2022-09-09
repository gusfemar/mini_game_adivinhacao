import sorteio
import titulos
import interacao_usuario

numero_sorteado = sorteio.numero_sorteado()
numero_de_tentativas = 0
tentativas_usuario = []

titulos.titulo_boas_vindas()

titulos.titulo_niveis()

nivel_de_dificuldade = interacao_usuario.pergunta_nivel()

dica = interacao_usuario.ajuda()


if nivel_de_dificuldade == 1:
    dificuldade =  8

elif nivel_de_dificuldade == 2:
    dificuldade = 5

else:
    dificuldade = 3

if dica == "s":

    dica = True

else:

    dica = False

while True:
    resposta_usuario = interacao_usuario.tentativa_usuario()

    if resposta_usuario != numero_sorteado:
        if resposta_usuario in tentativas_usuario:
            print("Esse número você já tentou!!!")

        else:
            tentativas_usuario.append(resposta_usuario)
            numero_de_tentativas += 1

            if dica == True:

                if resposta_usuario < numero_sorteado:
                    print("O número sorteado é maior!!!")

                else:
                    print("O número sorteado é menor!!!")

    if resposta_usuario == numero_sorteado:
        print("Parabéns, você acertou o número!!!")
        break

    if numero_de_tentativas == dificuldade:
        print(f"Número de tentativas excedido!!!")
        break
