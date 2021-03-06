#Calculadora Personalizada
# 1 - Soma
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisao
# 5 - R = (V, I)
# 6 - V = (r, I)
# 7 - I = (V, R)
# 8 - Req = série
# 9 - Req = paralelo
# 10 - Potência (R, I)

def  exibir_menu ():
  imprimir ( "Menu Calculadora:" )
  imprimir ( "1 - Somar" )
  imprimir ( "2 - Subtrair" )
  imprimir ( "3 - Multiplicar" )
  imprimir ( "4 - Dividir" )
  imprimir ( '5 - R = (V, I)' )
  imprimir ( '6 - V = (r, I)' )
  imprimir ( '7 - I = (V, R)' )
  imprimir ( '8 - Req = série' )
  imprimir ( '9 - Req = paralelo' )
  imprimir ( '10 - Potencia (R, I) ' )
  imprimir ( "0 - Sair" )

def  somar ( numero1 , numero2 ):
  retornar  numero1 + numero2

def  subtrair ( numero1 , numero2 ):
  return  numero1 - numero2

def  multiplicar ( numero1 , numero2 ):
  return  numero1 * numero2

def  dividir ( numero1 , numero2 ):
  se  numero2  ! =  0 :
    return  numero1 / numero2
  mais :
    return  "Divisão por zero!"

def  ohm1 ( tensao , corrente ):
  return  dividir ( tensao , corrente )

def  ohm2 ( resistencia , corrente ):
  retorno  multiplicar ( resistencia , corrente )

def  ohm3 ( tensao , resistencia ):
  return  dividir ( tensao , resistencia )

def  potencia ( resistencia , corrente ):
  retornar  resistencia  * ( corrente ** 2 )

def  serie ( resistencia1 , resistencia2 ):
  retornar  somar ( resistencia1 , resistencia2 )

def  paralelo ( resistencia1 , resistencia2 ):
  return  multiplicar ( resistencia1 , resistencia2 ) / somar ( resistencia1 , resistencia2 )

#Programa principal
importar  os
continuar  =  verdadeiro
enquanto  continuar  ==  Verdadeiro :
  os . sistema ( "limpar" ) #Sem janelas - cls
  exibir_menu ()
  opcao  =  int ( input ( "Opcao:" ))
  se  opcao  ==  1 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    print ( "Resultado:" , somar ( n1 , n2 ))
  elif  opcao  ==  2 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    imprimir ( "Resultado:" , subtrair ( n1 , n2 ))
  elif  opcao  ==  3 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    imprimir ( "Resultado:" , multiplicar ( n1 , n2 ))
  elif  opcao  ==  4 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    print ( "Resultado:" , dividir ( n1 , n2 ))
  elif  opcao  ==  5 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    print ( "Resultado:" , ohm1 ( n1 , n2 ))
  elif  opcao  ==  6 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    print ( "Resultado:" , ohm2 ( n1 , n2 ))
  elif  opcao  ==  7 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    imprimir ( "Resultado:" , ohm3 ( n1 , n2 ))
  elif  opcao  ==  8 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    imprimir ( "Resultado:" , serie ( n1 , n2 ))
  elif  opcao  ==  9 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    print ( "Resultado:" , paralelo ( n1 , n2 ))
  elif  opcao  ==  10 :
    n1  =  flutuante ( entrada ( "Numero 1:" ))
    n2  =  flutuante ( entrada ( "Numero 2:" ))
    print ( "Resultado:" , potencia ( n1 , n2 ))
  elif  opcao  ==  0 :
    continuar  =  False
  mais :
    imprimir ( "Opcao Invalida!" )
  entrada ( "Pressione, insira para continuar" )
