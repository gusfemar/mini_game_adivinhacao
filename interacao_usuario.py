def pergunta_nivel():
    """
    Pergunta ao usuário o nível de dificuldade desejado.
    :return: retorna 1, 2 ou 3.
    """
    return int(input("Selecione o nível de dificuldade (1, 2 ou 3): "))

def ajuda():
    """
    Pergunta ao usuário se deseja dicas ou não.
    :return: retorna sim ou não.
    """
    return str(input("Quer dicas [SIM/NÃO] ? ")).lower().strip()[0]

def tentativa_usuario():
    """
    Pergunta ao usuário sua tentativa.
    :return: retorna um número inteiro.
    """
    return int(input(f"ª tentativa: "))
