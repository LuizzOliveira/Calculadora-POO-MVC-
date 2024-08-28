import controller.calculadora_controller as c
import view as v




def execultarCalculadora():

   

    while True:

        v.menuCalculadora()

        menu= v.opcaoMenu()

        match menu:

            
            case 1:

                c.somar()


            case 2:

                c.subtrair()


            case 3:

                c.multiplicar()


            case 4:
                
                c.dividir()


            case 5:

                c.exponenciacao()

               
            case 6:

                c.raizQuadrada()
                
            
            case 7:

                c.porcentagem()


            case 8:

                c.restoDivisao()


            case 9:

                c.divisaoInteiro()


            case 0:
                v.sairMenu()
                break

            case _:
                v.opcaoInvalida()



execultarCalculadora()