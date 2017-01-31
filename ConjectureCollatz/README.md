# Conjectura de Collatz

É uma conjectura matemática que diz que quando o número for par, este número deve ser dividído por 2 e quando o número for ímpar, este número deve ser multiplicado por 3 e adicionar 1. 

    par: n = n / 2
    ímpar: n = (n * 3) + 1

Exemplo:

    Número inicial = 13

    13 é impar => (13 * 3) + 1 = 40     # 1 passo
    40 é par => 40 / 2 = 20             # 2 passo
    20 é par => 20 / 2 = 10             # 3 passo
    10 é par => 10 / 2 = 5              # 4 passo
    5 é impar => (5 * 3) + 1 = 16       # 5 passo
    16 é par => 16 / 2 = 8              # 6 passo
    8 é par => 8 / 2 = 4                # 7 passo
    4 é par => 4 / 2 = 2                # 8 passo
    2 é par => 2 / 2 = 1                # 9 passo
    1 é o número final.                 # 10 passo

Perceba que todo conjectura termina com a seguinte sequencia: [8, 4, 2, 1]

Este desafio consiste em executar essa conjectura matemática no menor tempo possível no intervalo de 0 a 1.000.000 com o tempo limite de 5 segundos, afim de verificar qual o número neste intervalo que possui a maior sequência de passos. Exemplo:

    collatz(13) => 10

Obs: Para solucionar este desafio no tempo limite será necessário reduzir o custo computacional para calcular a conjectura de Collatz.

Resposta: 837.799, quantidade de steps de 525.
