class Calculadora:
    def __init__(self) -> None:
        self.resultado = 0
        

    def soma(self, primeiroNumero, segundoNumero):

        self.resultado = primeiroNumero + segundoNumero
        return self.resultado
    

    def subtracao(self, primeiroNumero, segundoNumero):

        self.resultado = primeiroNumero - segundoNumero
        return self.resultado
    

    def multiplicacao(self, primeiroNumero, segundoNumero):

        self.resultado = primeiroNumero * segundoNumero
        return self.resultado
    

    def divisao(self, primeiroNumero, segundoNumero):

        self.resultado = primeiroNumero / segundoNumero
        return self.resultado
    

    def exponenciacao(self, primeiroNumero, segundoNumero):

        self.resultado = primeiroNumero ** segundoNumero
        return self.resultado
    

    def raizQuadrada(self, primeiroNumero):

        self.resultado = primeiroNumero ** 0.5
        return self.resultado
    

    def porcentagem(self, primeiroNumero, segundoNumero):

        percentual = primeiroNumero / 100
        self.resultado = segundoNumero * percentual

        return self.resultado
    

    def restoDivisao(self, primeiroNumero, segundoNumero):

        self.resultado = primeiroNumero % segundoNumero
        return self.resultado
    
    
    def divisaoInteiro(self, primeiroNumero, segundoNumero):

        self.resultado = primeiroNumero // segundoNumero
        return self.resultado