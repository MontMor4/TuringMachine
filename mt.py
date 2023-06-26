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
    direita = ">"
    esquerda = "<"
    cabecote = [] #Posição [0] = estado posição [1] = elemento
    
    # verica se a palavra pertence ao alfabeto     
    for i in palavra:
        if palavra[i] not in alfabeto:
            print('não')
            return
        
    #Iniciar trilha 1 com símbolo de inicio de vazio 
    palavra = caractere_inicio + caractere_vazio + palavra
    
    #Inicializar as outras trilhas com o tamanho da primeira palavra +2
    trilhas = [[] for _ in range(num_trilhas - 1)]  # Inicializa num_trilhas-1 arrays vazios
    for trilha in trilhas:
        trilha.extend([caractere_vazio] * len(palavra))  # Define o tamanho de cada array e preenche com valores vazios
        
    #Ler a palavra do terminal, e inicializar o cabecote
    cabecote = ["estado_inicial",palavra[0],trilhas[todos][0]] #Armazenar os símbolos das trilhas também na atual posição 
    for i in range(len(palavra)): #iterar cada caracter da palavra
        for j in range(len(transicoes)): #iterar cada trilha
            for k in range(len(num_trilhas)): #iterar cada transicao
                if palavra[i]==transicoes[j][k]: 
                    if trilha[k][i]==transicoes[j][k]:
                        

main()


