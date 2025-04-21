def distancia_edicao(str1, str2, memo=None):
    """
    Calcula a distância de Levenshtein entre duas strings utilizando recursão com memoização.
    
    A distância de Levenshtein é o número mínimo de operações de edição (inserção, exclusão, 
    substituição) necessárias para transformar uma string em outra.
    
    Args:
        str1 (str): Primeira string
        str2 (str): Segunda string
        memo (dict): Dicionário para memoização dos resultados
        
    Returns:
        int: Distância de edição entre as duas strings
    """
    # Inicialização do dicionário de memoização, se não fornecido
    if memo is None:
        memo = {}
    
    # Chave para o cache
    chave = (str1, str2)
    
    # Verifica se o resultado já está em cache
    if chave in memo:
        return memo[chave]
    
    # Casos base
    if len(str1) == 0:
        return len(str2)  # Precisamos inserir todos os caracteres de str2
    
    if len(str2) == 0:
        return len(str1)  # Precisamos excluir todos os caracteres de str1
    
    # Se os primeiros caracteres são iguais, não precisamos fazer nenhuma operação
    if str1[0] == str2[0]:
        custo = distancia_edicao(str1[1:], str2[1:], memo)
    else:
        # Caso contrário, escolhemos a operação de menor custo:
        # 1. Inserção (adicionar um caractere a str1)
        insercao = distancia_edicao(str1, str2[1:], memo) + 1
        
        # 2. Exclusão (remover um caractere de str1)
        exclusao = distancia_edicao(str1[1:], str2, memo) + 1
        
        # 3. Substituição (substituir um caractere de str1 por um de str2)
        substituicao = distancia_edicao(str1[1:], str2[1:], memo) + 1
        
        # Escolher a operação de menor custo
        custo = min(insercao, exclusao, substituicao)
    
    # Armazenar o resultado no cache
    memo[chave] = custo
    
    return custo

# Versão otimizada, tratando as strings como índices para melhorar a eficiência
def distancia_edicao_otimizada(str1, str2):
    """
    Versão otimizada da distância de Levenshtein usando índices em vez de fatias de string,
    que são mais eficientes.
    """
    memo = {}
    
    def dp(i, j):
        # Chave para o cache
        chave = (i, j)
        
        # Verifica se o resultado já está em cache
        if chave in memo:
            return memo[chave]
        
        # Casos base
        if i == 0:
            return j  # Precisamos inserir j caracteres
        
        if j == 0:
            return i  # Precisamos excluir i caracteres
        
        # Se os caracteres são iguais, não precisamos fazer nenhuma operação
        if str1[i-1] == str2[j-1]:
            memo[chave] = dp(i-1, j-1)
        else:
            # Escolher a operação de menor custo
            memo[chave] = 1 + min(
                dp(i, j-1),      # Inserção
                dp(i-1, j),      # Exclusão
                dp(i-1, j-1)     # Substituição
            )
        
        return memo[chave]
    
    return dp(len(str1), len(str2))

# Função para mostrar o caminho de edição entre duas strings
def mostrar_caminho_edicao(str1, str2):
    """
    Mostra o caminho de edição mínimo entre duas strings.
    Retorna a sequência de operações necessárias.
    """
    # Primeiro, construímos a matriz de distância completa
    m, n = len(str1), len(str2)
    
    # Inicializar a matriz com valores infinitos
    dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Caso base: transformar string vazia em outra string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Preencher a matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # Sem custo para caracteres iguais
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Exclusão
                    dp[i][j-1],    # Inserção
                    dp[i-1][j-1]   # Substituição
                )
    
    # Reconstruir o caminho
    operacoes = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i-1] == str2[j-1]:
            # Caracteres iguais, não faz nada
            operacoes.append(f"Manter '{str1[i-1]}'")
            i -= 1
            j -= 1
        else:
            if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
                # Substituição
                operacoes.append(f"Substituir '{str1[i-1]}' por '{str2[j-1]}'")
                i -= 1
                j -= 1
            elif j > 0 and dp[i][j] == dp[i][j-1] + 1:
                # Inserção
                operacoes.append(f"Inserir '{str2[j-1]}'")
                j -= 1
            else:
                # Exclusão
                operacoes.append(f"Excluir '{str1[i-1]}'")
                i -= 1
    
    operacoes.reverse()
    return operacoes

# Exemplos de uso
if __name__ == "__main__":
    # Exemplos básicos
    print("Exemplo 1: Transformar 'kitten' em 'sitting'")
    resultado = distancia_edicao('kitten', 'sitting')
    resultado_otimizado = distancia_edicao_otimizada('kitten', 'sitting')
    print(f"Distância de edição: {resultado}")
    print(f"Distância de edição (otimizada): {resultado_otimizado}")
    print("Caminho de edição:")
    for op in mostrar_caminho_edicao('kitten', 'sitting'):
        print(f"  - {op}")
    print()
    
    print("Exemplo 2: Transformar 'sunday' em 'saturday'")
    resultado = distancia_edicao('sunday', 'saturday')
    resultado_otimizado = distancia_edicao_otimizada('sunday', 'saturday')
    print(f"Distância de edição: {resultado}")
    print(f"Distância de edição (otimizada): {resultado_otimizado}")
    print("Caminho de edição:")
    for op in mostrar_caminho_edicao('sunday', 'saturday'):
        print(f"  - {op}")
    print()
    
    # Exemplo de caso extremo
    print("Exemplo 3: Strings completamente diferentes")
    resultado = distancia_edicao('abc', 'xyz')
    resultado_otimizado = distancia_edicao_otimizada('abc', 'xyz')
    print(f"Distância de edição: {resultado}")
    print(f"Distância de edição (otimizada): {resultado_otimizado}")
    print("Caminho de edição:")
    for op in mostrar_caminho_edicao('abc', 'xyz'):
        print(f"  - {op}")
    print()
    
    # Exemplo de caso nulo
    print("Exemplo 4: String vazia para outra string")
    resultado = distancia_edicao('', 'abc')
    resultado_otimizado = distancia_edicao_otimizada('', 'abc')
    print(f"Distância de edição: {resultado}")
    print(f"Distância de edição (otimizada): {resultado_otimizado}")
    print("Caminho de edição:")
    for op in mostrar_caminho_edicao('', 'abc'):
        print(f"  - {op}")
    print()
    
    # Exemplo de strings iguais
    print("Exemplo 5: Strings idênticas")
    resultado = distancia_edicao('abc', 'abc')
    resultado_otimizado = distancia_edicao_otimizada('abc', 'abc')
    print(f"Distância de edição: {resultado}")
    print(f"Distância de edição (otimizada): {resultado_otimizado}")
    print("Caminho de edição:")
    for op in mostrar_caminho_edicao('abc', 'abc'):
        print(f"  - {op}")
    print() 