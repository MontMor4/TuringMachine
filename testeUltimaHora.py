import json
import sys

def main():

    # Verificar se a quantidade correta de argumentos foi fornecida
    # if len(sys.argv) != 3:
    #     print('Usar: ./mt [MT] [Word]')
    #     exit()

    # Argumentos da linha de comando
    arquivo_json = 'mt.json' #sys.argv[1]
    palavra = '1' #sys.argv[2]

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

    # Verificar se a palavra pertence ao alfabeto
    for i in palavra:
        if i not in alfabeto:
            print('não')
            return
        
    # Iniciar trilha 1 com símbolo de início de vazio
    palavra = caractere_inicio + palavra + caractere_vazio
    
    # Inicializar as outras trilhas com o tamanho da primeira palavra atualizada
    trilhas = [[] for _ in range(num_trilhas-1)]  # Inicializa num_trilhas-1 arrays vazios
    
    for trilha in trilhas:
        trilha.extend([caractere_vazio] * len(palavra))  # Define o tamanho de cada array e preenche com valores vazios
    trilhas = [list(palavra)] + trilhas


    estado_atual = estado_inicial
    cabecote = 1
    num_transicoes = len(transicoes) 
    
    # UUUUUUUUUUUUU  
    # <101021023011
    #      |
    
    while True:
        
        for i in range(num_transicoes):
            fez_transicao = True
            
            if estado_atual == transicoes[i][0]:
                for j in range(num_trilhas):
                    if trilhas[j][cabecote] != transicoes[i][j+1]:
                        fez_transicao = False
                        break
                    
            else: 
                if i != num_transicoes-1: continue
            
            if(fez_transicao):
                estado_atual = transicoes[i][1 + num_trilhas]
                for j in range(num_trilhas):                    
                    trilhas[j][cabecote] = transicoes[i][j + num_trilhas + 2]
                        
                #Pegar o último simbolo da transição, se for < cabecote-- ou se for >cabecote++
                if transicoes[i][-1] == '<': cabecote -= 1
                else: 
                    cabecote += 1
                    if cabecote >= len(trilhas[j]):
                        for k in range (num_trilhas):
                            trilhas[k] += caractere_vazio
                break
        
        if cabecote < 0: break
        
        if not fez_transicao:
            if estado_atual in estado_final: print('Sim')
            else: print('Não')
            return
        
    print('Não')
    return
        

main()
