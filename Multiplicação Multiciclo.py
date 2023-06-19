def main():
    fator1 = IntParaBinario(int(input("Digite o primeiro número: ")))
    fator2 = IntParaBinario(int(input("Digite o segundo numero número: ")))
    MultipicacaoBinaria(fator1, fator2)


def IntParaBinario(numero): #FUNÇÃO QUE TRANSFORMA INT EM BINARIOS
    representacaoBinaria = []
    while numero > 0:
        representacaoBinaria.insert(0, numero % 2)
        numero //= 2
    return representacaoBinaria

def MultipicacaoBinaria(multiplicando, multiplicador):
    multiplicando = [0 for digito in multiplicando] + multiplicando #DOBRANDO A QUANTIDADE DE BITS DO multiplicando
    produto = [0 for digito in multiplicando] # CRIANDO X BITS VAZIOS COM O TAMNHO DO multiplicando
    print("inicio: ")
    print(f"multiplicando: {multiplicando} - ", end="")
    print(f"multiplicador: {multiplicador} - ", end="")
    print(f"produto: {produto}")
    for i in range(len(multiplicador)): #QUANTIDADE DE CICLOS DEFINIDA PELO TAMANHO DO multiplicador
        if multiplicador[-1] == 1: #CHECANDO SE O ULTIMO BIT DO multiplicador É 1
            produto = SomaBinaria(multiplicando, produto) #FUNÇÃO IMPLEMENTADA A BAIXO QUE SOMA DOIS BINARIOS
        multiplicador = [0] + [digito for digito in multiplicador[:-1]] #SHIFT RIGHT
        multiplicando = [digito for digito in multiplicando[1:]] + [0]  #SHIFT LEFT
        print(f"Ciclo numero {i+1}")
        print(f"multiplicando: {multiplicando} - ", end="")
        print(f"multiplicador: {multiplicador} - ", end="")
        print(f"produto: {produto}")
    print(f"Resultado final {produto}")         

def SomaBinaria(binario1, binario2):
    binario1 = binario1[::-1] #INVERTENDO OS BITS POIS PRECISAMOS TRABALHAR DE TRAS PARA FRENTE
    binario2 = binario2[::-1]
    soma = [0 for digito in binario1] #CRIANDO UM RESULTADO ZERADO
    for i in range(len(binario1)):
        if binario1[i] + binario2[i] + soma[i] == 0: #CHECANDO A SOMA DOS DIGITOS NA MESMA POSICAO
            soma[i] = 0
        elif binario1[i] + binario2[i] + soma[i] == 1:
            soma[i] = 1
        elif binario1[i] + binario2[i] + soma[i] == 2:
            soma[i] = 0
            if i < len(soma): #PRECISAMOS CHECAR SE NAO ESTAMOS NO ULTIMO BIT
                soma[i+1] = 1
        elif binario1[i] + binario2[i] + soma[i] == 3:
            soma[i] = 1
            if i < len(soma):
                soma[i+1] = 1
    return soma[::-1]


main()




