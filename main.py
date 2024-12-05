import numpy as np
# Para exemplificar melhor, usaremos nomes de sites de acordo com letras do alfabeto, e logo limitaremos os exemplos em até 26 sites.
letrasAfabetoParaNomesSites = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def FormarMatrizDeTransicao():
    quantidadeSites = int(input("Quantos sites haverão para o exemplo do algoritmo de PageRank? (2 a 26 sites) - "))
    while(quantidadeSites < 2 or quantidadeSites > 26):
        quantidadeSites = int(input("Número inválido, para o exemplo, re-digite uma quantidade entre o seguinte limite: 2 a 26 sites - "))
    matrizTransicoes = np.zeros(shape=(quantidadeSites, quantidadeSites))
    for i in range(quantidadeSites):
        input_sitesApontados = input("Para quais sites que site {} aponta? (Ex.: A B D G J / Ex. no caso de não apontar para nenhum site: 0)\n".format(letrasAfabetoParaNomesSites[i])) 
        if(input_sitesApontados == "0"):
            for j in range(quantidadeSites):
                matrizTransicoes[j][i] = 1/quantidadeSites
        else:
            sitesApontados = input_sitesApontados.split()
            for j in range(quantidadeSites):
                if(letrasAfabetoParaNomesSites[j] in sitesApontados):
                    matrizTransicoes[j][i] = 1/len(sitesApontados)
    return matrizTransicoes

def PageRank(matrizTransicoes, fatorAmortecimento = 0.15):
    # Definição do total de linhas que compõem a matriz de transição (quantidade de sites)
    linhas = matrizTransicoes.shape[0]

    # Vetor inicial com probabilidade igual para todos os sites 
    v = np.zeros(shape=(linhas, 1))
    for linha in range(linhas):
        v[linha][0] = 1/linhas
    
    # Fórmula que define a matriz inicial de PageRank
    matrizPageRank = (1 - fatorAmortecimento) * matrizTransicoes + fatorAmortecimento * (1/linhas) * np.ones((linhas, linhas))
    
    # Criação de vetor auxiliar
    auxV = np.zeros(shape=(linhas, 1))
    for indice in range(linhas):
        auxV = v.copy()
        v = matrizPageRank.dot(v)

    matrizPageRank = v/np.sum(v)

    return matrizPageRank

# Função que imprime as informações sobre o ranking dos sites mais influentes
def ImprimirResultadosPageRank(matrizPageRank):
    print("Ranking dos sites mais influentes:")
    matrizPageRankOrdenado = sorted(matrizPageRank, reverse=True)
    for ind in range(matrizPageRank.shape[0]):
        indAlfabeto = np.where(matrizPageRank == matrizPageRankOrdenado[ind])
        print("{}. Site {}".format(ind + 1, letrasAfabetoParaNomesSites[indAlfabeto[0][0]]))
        # Para o caso de valores da matriz de PageRank serem iguais
        if(len(indAlfabeto[0]) > 1):
            matrizPageRank[indAlfabeto[0][0]] = 0
    print("\n")

def main():
    matrizTransicoes = FormarMatrizDeTransicao()
    print("Matriz de Transição:\n\n{}\n\n".format(matrizTransicoes))
    matrizPageRank = PageRank(matrizTransicoes)
    print("Matriz da PageRank:\n\n{}\n\n".format(matrizPageRank))
    ImprimirResultadosPageRank(matrizPageRank)

if __name__ == "__main__":
    main()