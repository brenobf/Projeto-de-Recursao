# Projeto de Recursão

1. Sobre o projeto

Este projeto tem como objetivo compreender o funcionamento da recursão em Python, analisando como uma função pode chamar a si mesma para resolver problemas e quais são os custos computacionais envolvidos nesse processo.

O projeto aborda três problemas clássicos da programação:

- Fatorial;
- Sequência de Fibonacci;
- Torre de Hanói.

Também apresenta comparações entre algoritmos recursivos e iterativos, contagem de chamadas, visualização da pilha de execução e exemplos gráficos de recursão.

2. Objetivos

- Compreender o funcionamento da recursão.
- Identificar os casos base e as chamadas recursivas.
- Comparar soluções recursivas e iterativas.
- Analisar o custo computacional dos algoritmos.
- Visualizar a execução de funções recursivas.
- Demonstrar aplicações práticas da recursão.

3. Tecnologias utilizadas

O projeto foi desenvolvido utilizando Python 3.

Bibliotecas utilizadas:

| Biblioteca | Finalidade |
| `tkinter` | Construção da interface gráfica. |
| `ttk` | Componentes visuais e organização das abas. |
| `time` | Medição do tempo de execução. |
| `turtle` | Desenho da árvore fractal. |

4. Funcionalidades implementadas

4.1. Fatorial

Implementação de duas abordagens:

- Recursiva: a função chama a si mesma até alcançar o caso base.
- Iterativa: utiliza uma estrutura de repetição para calcular o resultado.

4.2. Fibonacci

Implementação de três abordagens:

- Recursiva: realiza chamadas para os dois termos anteriores da sequência.
- Iterativa: utiliza variáveis para calcular os termos progressivamente.
- Memoização: armazena resultados já calculados para evitar repetições desnecessárias.

4.3. Contagem de chamadas

O programa contabiliza quantas vezes a função Fibonacci recursiva é executada para:

- N = 10;
- N = 20;
- N = 30.

A contagem inclui as chamadas dos casos base.

4.4. Torre de Hanói

Implementação recursiva do problema da Torre de Hanói.

O algoritmo calcula a sequência de movimentos necessários para transferir todos os discos de uma torre para outra, respeitando as regras:

1. Mover apenas um disco por vez.
2. Mover somente o disco que estiver no topo de uma torre.
3. Nunca colocar um disco maior sobre um disco menor.

O programa também apresenta uma animação gráfica dos movimentos.

A quantidade mínima de movimentos é calculada pela fórmula:

M(n) = 2ⁿ − 1

Para três discos, são necessários exatamente sete movimentos.

4.5. Visualização da pilha de chamadas

Apresenta uma representação textual das chamadas do Fibonacci, mostrando a profundidade de cada chamada e identificando os casos base.

4.6. Árvore fractal

Utiliza a biblioteca Turtle para desenhar uma árvore fractal.

O desenho é construído recursivamente: cada galho gera dois galhos menores, até alcançar a condição de parada.

----------------------------------------------------------------------------------------------------------

5. Pseudocódigo dos algoritmos

O pseudocódigo representa a lógica dos algoritmos de maneira simplificada, sem depender da sintaxe de uma linguagem de programação específica.

5.1. Fatorial recursivo

FUNÇÃO FATORIAL_RECURSIVO(n)

    SE n <= 1 ENTÃO
        RETORNE 1
    FIM SE

    RETORNE n * FATORIAL_RECURSIVO(n - 1)

FIM FUNÇÃO

Explicação: a função multiplica o número atual pelo resultado do fatorial do número anterior, até alcançar o caso base.

5.2. Fatorial iterativo

FUNÇÃO FATORIAL_ITERATIVO(n)

    resultado <- 1

    PARA i DE 2 ATÉ n FAÇA
        resultado <- resultado * i
    FIM PARA

    RETORNE resultado

FIM FUNÇÃO

Explicação: utiliza uma estrutura de repetição para multiplicar os números progressivamente.

5.3. Fibonacci recursivo

FUNÇÃO FIBONACCI_RECURSIVO(n)

    SE n <= 1 ENTÃO
        RETORNE n
    FIM SE

    RETORNE FIBONACCI_RECURSIVO(n - 1)
           + FIBONACCI_RECURSIVO(n - 2)

FIM FUNÇÃO

Explicação: cada chamada calcula a soma dos dois termos anteriores da sequência. Os casos base são F(0) = 0 e F(1) = 1.

5.4. Fibonacci iterativo

FUNÇÃO FIBONACCI_ITERATIVO(n)

    a <- 0
    b <- 1

    PARA i DE 0 ATÉ n - 1 FAÇA
        temporario <- a + b
        a <- b
        b <- temporario
    FIM PARA

    RETORNE a

FIM FUNÇÃO

Explicação: utiliza duas variáveis para armazenar os termos anteriores e calcular o próximo valor sem chamadas recursivas.

5.5. Fibonacci com memoização

FUNÇÃO FIBONACCI_MEMOIZADO(n, memoria)

    SE n ESTÁ EM memoria ENTÃO
        RETORNE memoria[n]
    FIM SE

    SE n <= 1 ENTÃO
        RETORNE n
    FIM SE

    memoria[n] <- FIBONACCI_MEMOIZADO(n - 1, memoria)
                  + FIBONACCI_MEMOIZADO(n - 2, memoria)

    RETORNE memoria[n]

FIM FUNÇÃO

Explicação: armazena os resultados já calculados para evitar que a função repita cálculos desnecessários.

5.6. Contagem de chamadas do Fibonacci

FUNÇÃO FIBONACCI_CONTADOR(n)

    chamadas <- 0

    FUNÇÃO CALCULAR(k)

        chamadas <- chamadas + 1

        SE k <= 1 ENTÃO
            RETORNE k
        FIM SE

        RETORNE CALCULAR(k - 1) + CALCULAR(k - 2)

    FIM FUNÇÃO

    resultado <- CALCULAR(n)

    RETORNE resultado, chamadas

FIM FUNÇÃO

Explicação: utiliza uma variável para contabilizar todas as entradas na função, inclusive os casos base.

5.7. Torre de Hanói recursiva

FUNÇÃO TORRE_HANOI(n, origem, destino, auxiliar)

    SE n = 1 ENTÃO
        MOVER disco da origem para o destino
        RETORNAR
    FIM SE

    TORRE_HANOI(n - 1, origem, auxiliar, destino)

    MOVER disco da origem para o destino

    TORRE_HANOI(n - 1, auxiliar, destino, origem)

FIM FUNÇÃO

Explicação: transfere os discos menores para a torre auxiliar, move o maior disco para o destino e, em seguida, transfere os discos menores para a torre final.

5.8. Árvore fractal

FUNÇÃO GALHO(tamanho, nivel)

    SE nivel = 0 OU tamanho < 5 ENTÃO
        RETORNAR
    FIM SE

    DESENHAR galho para frente

    GIRAR 30 GRAUS PARA A DIREITA
    GALHO(tamanho * 0.7, nivel - 1)

    GIRAR 60 GRAUS PARA A ESQUERDA
    GALHO(tamanho * 0.7, nivel - 1)

    GIRAR 30 GRAUS PARA A DIREITA

    VOLTAR ao ponto inicial do galho

FIM FUNÇÃO

Explicação: cada galho gera dois novos galhos menores, repetindo o processo até atingir a condição de parada.

6. Análise da pilha de chamadas

Exemplo de execução do Fibonacci para n = 3:

FIB(3)
│
├── FIB(2)
│   ├── FIB(1) → Caso base
│   └── FIB(0) → Caso base
│
└── FIB(1) → Caso base


Resultado:

FIB(3) = 2

Total de chamadas = 5


A pilha de chamadas armazena temporariamente as funções que ainda precisam concluir sua execução. Quando um caso base é alcançado, a função retorna o resultado para a chamada anterior.

7. Complexidade dos algoritmos

| Algoritmo | Tempo | Espaço auxiliar |
|---|---|---|
| Fatorial recursivo | O(n) | O(n) |
| Fatorial iterativo | O(n) | O(1) |
| Fibonacci recursivo | O(2ⁿ) | O(n) |
| Fibonacci iterativo | O(n) | O(1) |
| Fibonacci memoizado | O(n) | O(n) |
| Torre de Hanói | O(2ⁿ) | O(n) |

Observação: a complexidade da Torre de Hanói considera a quantidade de movimentos, enquanto o espaço auxiliar considera a profundidade da recursão.
