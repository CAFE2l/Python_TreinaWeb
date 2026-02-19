cores = {
    "limpa": "\033[m",
    'vermelho': "\033[31m",
    'verde': "\033[32m",
    'amarelo': "\033[33m",
    'azul': "\033[34m",
    'roxo': "\033[35m",
    'ciano': "\033[36m",
    'cinza': "\033[37m",
    'pretoebranco': '\033[7;30m'
}

fundo = {
    "branco": "\033[40m",
    'vermelho': "\033[41m",
    'verde': "\033[42m",
    'amarelo': "\033[43m",
    'azul': "\033[44m",
    'roxo': "\033[45m",
    'ciano': "\033[46m",
    'cinza': "\033[47m",
    'vermelho_claro': '\033[101m',
    'verde_claro': '\033[102m',
    'amarelo_claro': '\033[103m',
    'azul_claro': '\033[104m',
    'roxo_claro': '\033[105m',
    'ciano_claro': '\033[106m',
    'cinza_claro': '\033[107m'
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m",
    "duplosublinhado": "\033[21m",
    "normal": "\033[22m",
    "semitalico": "\033[23m",
    "sem_sublinhado": "\033[24m",
    "sem_inverso": "\033[27m",
    "visivel": "\033[28m",
    "sem_tachado": "\033[29m"
}
frase = "Aprendendo sobre arrays"

print(f"{estilos['negrito']}{cores['azul']}{"==="*4}{cores['cinza']}Vetores{cores['verde']}{"==="*5}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 



# 0 / 1 / 2 / 3 / 4 
# 5 / 2 / 4 / 6 / 1
numeros = list()
tamanho = int(input(f"{estilos['negrito']}{cores['cinza']}Digite o tamanho do vetor: "))
for i in range(tamanho):
    #0 ... 5
    valor = int(input(f"Digite o número do vetor na posição {cores['vermelho']}{i}:{cores['cinza']} "))
    numeros.append(valor)
print(f"{cores['cinza']}Vetor: {cores['azul']}{numeros}")
print(f"{cores['cinza']}Valor da {cores['verde']}Primeira{cores['cinza']} posição: {numeros[0]}")

# BUSCA LINEAR
numero_pesquisar = int(input(f"{cores['cinza']}{estilos['negrito']}Digite o valor a ser pesquisado no vetor: "))
posicao_resultado = -1
for i in range(tamanho):
    #0 .. 5
    if numeros[i] == numero_pesquisar:
        posicao_resultado = i
        break
if posicao_resultado < 0: 
    print(f"{cores['vermelho']}{estilos['italico']}O elemento não foi encontrado no vetor{cores['limpa']}")
else:
    print(f"Elemento encontrado na posição {estilos['italico']}{cores['verde']}{posicao_resultado}")

# FIM BUSCA LINEAR
# SELECTION SORT
# 0 / 1 / 2 / 3 / 4
# 5 / 2 / 4 / 6 / 1
# 1 / 2 / 4 / 6 / 5
# 1 / 2 / 4 / 5 / 6

for i in range(tamanho):
    indice_menor = i
    for j in range(int(i + 1), tamanho):
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print(f"vetor: {numeros}")



# FIM SELECTION SORT
