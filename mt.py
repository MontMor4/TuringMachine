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
    print(palavra)
    # Inicializar as outras trilhas com o tamanho da primeira palavra + 2
    trilhas = [[] for _ in range(num_trilhas-1)]  # Inicializa num_trilhas-1 arrays vazios
    for trilha in trilhas:
        trilha.extend([caractere_vazio] * len(palavra))  # Define o tamanho de cada array e preenche com valores vazios
    trilhas = [palavra] + trilhas

main()
