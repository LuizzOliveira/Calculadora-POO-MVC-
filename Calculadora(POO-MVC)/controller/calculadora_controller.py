from model.calculadora import Calculadora
import view as v

resultado = Calculadora()


def somar():

    try:

        num1 = v.primeiroNumero()

        num2 =v.segundoNumero()
        
        v.verResultado(resultado.soma(num1, num2))
        
    except:

        return v.numInvalido()
    



def subtrair():

    try:
        num1 = v.primeiroNumero()

        num2 = v.segundoNumero()

        v.verResultado(resultado.subtracao(num1, num2))

    except:

        return v.numInvalido()
    


def multiplicar():

    try:

        num1 = v.primeiroNumero()

        num2 = v.segundoNumero()

        v.verResultado(resultado.multiplicacao(num1, num2))
    
    except:

        return v.numInvalido()
    


def dividir():

    try:

        num1= v.dividendo()

        num2= v.divisor()

        if num2 != 0:

            v.verResultado(resultado.divisao(num1, num2))

        else:
            v.divisorZero()

        

    except:

        return v.numInvalido()
    



def exponenciacao():

    try:

        num1 = v.baseExpoenciacao()
        
        num2 = v.expoente()

        v.verResultado(resultado.exponenciacao(num1, num2))

    except:

        return v.numInvalido()
    



def raizQuadrada():

    try:

        num= v.numeroRaizQuadrada()

        v.verResultado(resultado.raizQuadrada(num))

    except:

        return v.numInvalido()
    





def porcentagem():

    try:

        num1= v.porcentagem()

        num2= v.numPorcentagem()
        
        v.verResultado(resultado.porcentagem(num1, num2))

    except:

        return v.numInvalido()
    



def restoDivisao():

    try:

        num1 = v.primeiroNumero()

        num2 = v.segundoNumero()

        v.verResultado(resultado.restoDivisao(num1, num2))

    except:

        return v.numInvalido()
    



def divisaoInteiro():

    try:

        num1 = v.primeiroNumero()

        num2 = v.segundoNumero()

        v.verResultado(resultado.divisaoInteiro(num1, num2))

    except:

        return v.numInvalido()