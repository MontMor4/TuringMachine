import json
import sys

def main():

    # Verificar se a quantidade correta de argumentos foi fornecida
    if len(sys.argv) != 3:
        print('Usar: ./mt [MT] [Word]')
        exit()

    # Argumentos da linha de comando
    arquivo_json = sys.argv[1]
    palavra = sys.argv[2]

    # Carregar dados do JSON
    with open(arquivo_json) as arquivo:
        dados = json.load(arquivo)
        mt = dados['mt']

    num_trilhas = mt[0]
    estados = mt[1]
    alfabeto = mt[2]
    nao_usado = mt[3]
    caractere_inicio = mt[4]
    caractere_vazio = mt[5]
    transicoes = mt[6]
    estado_inicial = mt[7]
    estado_final = mt[8]
    cabecote = []  # Posição [0] = estado posição [1] = elemento
    count = 0
    binarioParada = 0

    # Verificar se a palavra pertence ao alfabeto
    for i in palavra:
        if i not in alfabeto:
            print('não')
            return

    # Iniciar trilha 1 com símbolo de início de vazio
    palavra = caractere_inicio + caractere_vazio + palavra

    # Inicializar as outras trilhas com o tamanho da primeira palavra + 2
    trilhas = [[] for _ in range(num_trilhas - 1)]  # Inicializa num_trilhas-1 arrays vazios
    for trilha in trilhas:
        trilha.extend([caractere_vazio] * len(palavra))  # Define o tamanho de cada array e preenche com valores vazios
    trilhas[0].append(palavra)
    cabecote.append(estado_inicial)
    for j in range(len(trilhas)):
        cabecote.append(trilhas[j][0])

    for p in range(len(palavra)):
        for t in transicoes:
            for x in range(1, len(transicoes[t]) - 1):
                if transicoes[t][0] == cabecote[0]:
                    for z in range(len(trilhas)):
                        if transicoes[t][x] == cabecote[z+1]:
                            count += 1
                if count == len(trilhas):
                    binarioParada = 1
                    cabecote[0] = transicoes[t][x]
                    for z in range(len(trilhas)):
                        trilhas[z][0] = cabecote[z+1]
                    # Substituir do cabeçote na palavra
                    palavra = palavra[:p] + cabecote[0] + palavra[p+1:]

                # Fazer condição de parada agora, posso criar um binário da parada
            if binarioParada == 0:
                if cabecote[0] in estado_final:
                    print('sim')
                    return
                else:
                    print('nao')
                    return
            if binarioParada == 1:
                binarioParada = 0

            if transicoes[t][-1] == '<':
                p = -1

            # Verificar se é direita ou esquerda caso não tenha ocorrido a parada
            # Agora percorrer toda a palavra e depois as trilha e ver se encaixa em alguma transicao


main()
