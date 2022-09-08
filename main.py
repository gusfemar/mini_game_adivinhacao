from random import randint

numero_sorteado = randint(1, 10)
numero_de_tentativas = 0
tentativas_usuario = []

print("Bem vindo ao jogo da adivinhação!!!")

print("""Níveis de dificuldade:
1 - Fácil - 8 tentativas
2 - Médio - 5 tentativas
3 - Difícil - 3 tentativas""")

nivel_de_dificuldade = int(input("Selecione o nível de dificuldade (1, 2 ou 3): "))

dica = str(input("Quer dicas [SIM/NÃO] ? ")).lower().strip()[0]

if nivel_de_dificuldade == 1:
    dificuldade = 8

elif nivel_de_dificuldade == 2:
    dificuldade = 5

else:
    dificuldade = 3

if dica == "s":

    dica = True

else:

    dica = False

while True:
    resposta_usuario = int(input(f"{numero_de_tentativas + 1}ª tentativa: "))

    if resposta_usuario == numero_sorteado:
        print("Parabéns, você acertou o número!!!")
        break

    elif resposta_usuario != numero_sorteado:
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

    if numero_de_tentativas == dificuldade:
        print(f"Número de tentativas excedido!!!")
        break