# Distância de Edição (Levenshtein Distance) com Memoização

Este projeto implementa o algoritmo de Distância de Levenshtein utilizando recursão com memoização (programação dinâmica).

## Acadêmicos

- Arthur Henrique Tscha Vieira
- Rafael Rodrigues Ferreira de Andrade

## Descrição do Problema

A **Distância de Levenshtein** (ou Distância de Edição) é uma métrica que mede o número mínimo de operações elementares necessárias para transformar uma string em outra. As operações permitidas são:

1. **Inserção**: adicionar um caractere
2. **Exclusão**: remover um caractere
3. **Substituição**: trocar um caractere por outro

Por exemplo, para transformar a palavra "kitten" em "sitting", precisamos de 3 operações:

- Substituir 'k' por 's' ("sitten")
- Substituir 'e' por 'i' ("sittin")
- Inserir 'g' no final ("sitting")

## Implementação

O projeto contém três implementações principais:

1. **distancia_edicao()**: Implementação recursiva direta com memoização usando um dicionário Python (hashtable).
2. **distancia_edicao_otimizada()**: Versão otimizada que usa índices em vez de operações de slice de string, melhorando a eficiência.
3. **mostrar_caminho_edicao()**: Função que mostra o caminho de edição mínimo entre duas strings, exibindo as operações necessárias para a transformação.

### Como funciona a memoização

A solução utiliza um dicionário Python (`dict`) como cache para armazenar resultados já calculados:

- A chave é um par de strings ou índices, dependendo da implementação
- O valor é a distância de edição mínima para esse par
- Antes de cada cálculo recursivo, verificamos se o resultado já existe no cache
- Após calcular um novo resultado, ele é armazenado no cache para uso futuro

Isso reduz a complexidade de tempo de O(3^n) para O(m\*n), onde m e n são os comprimentos das strings.

## Como executar

Para executar o código com os exemplos incluídos:

```bash
python edit_distance.py
```

O programa exibirá:

- A distância de edição entre cada par de strings
- O caminho detalhado de edição, mostrando cada operação necessária

## Exemplo de saída

```
Exemplo 1: Transformar 'kitten' em 'sitting'
Distância de edição: 3
Caminho de edição:
  - Substituir 'k' por 's'
  - Manter 'i'
  - Manter 't'
  - Manter 't'
  - Substituir 'e' por 'i'
  - Manter 'n'
  - Inserir 'g'
```

## Complexidade

- **Tempo**: O(m\*n) onde m e n são os comprimentos das strings
- **Espaço**: O(m\*n) para o cache de memoização
