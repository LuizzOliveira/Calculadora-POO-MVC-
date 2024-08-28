def menuCalculadora():
    print("\n ############################")
    print(" *     CALCULADORA          *")
    print(" *                          *")
    print(" * (1). ADIÇÃO              *")
    print(" * (2). SUBTRAÇÃO           *")
    print(" * (3). MULTIPLICAÇÃO       *")
    print(" * (4). DIVISÃO             *")
    print(" * (5). EXPONENCIAÇÃO       *")
    print(" * (6). RAIZ QUADRADA       *")
    print(" * (7). PORCENTAGEM         *")
    print(" * (8). RESTO DA DIVISÃO    *")
    print(" * (9). DIVISÃO DE INTEIRO  *")
    print(" * (0). SAIR DO PROGRAMA    *")
    print(" *                          *")
    print(" ############################\n")

def verResultado(resultado):
    print("\nResultado: ", resultado)

def primeiroNumero():
    return float(input("\nDigite o primeiro número: "))

def segundoNumero():
    return float(input("\nDigite o segundo número: "))

def numInvalido():
    print("\nDigite apenas números!")

def dividendo():
    return float(input("\nInforme o numero para ser dividido: "))

def divisor():
    return float(input("\nInforme o divisor : "))

def divisorZero():
    print("\nDivisor precisa ser diferente de Zero!")

def baseExpoenciacao():
    return float(input("\nDigite a base para a exponenciação: "))

def expoente():
    return float(input("\nDigite o expoente para a exponenciação: "))

def numeroRaizQuadrada():
    return float(input("\nDigite o número para calcular a raiz quadrada: "))

def porcentagem():
    return float(input("\nDigite a porcentagem (sem o símbolo %): "))

def numPorcentagem():
    return float(input("\nInforme número para calcular a porcentagem: "))

def opcaoMenu():
    try:
        return float(input("Opção Menu: "))
    except:
        pass

def sairMenu():
    print("\n  Você Saiu!")

def opcaoInvalida():
    print("\nOpção inválida. Escolha uma opção entre 1 e 9 ou 0 para sair.")