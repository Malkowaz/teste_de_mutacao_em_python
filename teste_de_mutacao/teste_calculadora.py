import unittest
from calculadora import *

class Teste_calculadora(unittest.TestCase):
     
    def teste_soma(self):
       #Recebe o valor 'ABCDE' e retorna 'ABCDE'
       
        entrada_n1 = 3
        entrada_n2 = 4
        entrada_escolha = '1'
        esperado = 7.0
        resultado = calculadora(entrada_n1,entrada_n2,entrada_escolha)

        assert resultado == esperado

    def teste_subtracao(self):
       #Recebe o valor 'ABCDE' e retorna 'ABCDE'
       
        entrada_n1 = 10
        entrada_n2 = 4
        entrada_escolha = '2'
        esperado = 6.0
        resultado = calculadora(entrada_n1,entrada_n2,entrada_escolha)

        assert resultado == esperado

    def teste_multiplicacao(self):
       #Recebe o valor 'ABCDE' e retorna 'ABCDE'
       
        entrada_n1 = 10
        entrada_n2 = 4
        entrada_escolha = '3'
        esperado = 40.0
        resultado = calculadora(entrada_n1,entrada_n2,entrada_escolha)

        assert resultado == esperado

    def teste_divisao(self):
       #Recebe o valor 'ABCDE' e retorna 'ABCDE'
       
        entrada_n1 = 5
        entrada_n2 = 5
        entrada_escolha = '4'
        esperado = 1.0
        resultado = calculadora(entrada_n1,entrada_n2,entrada_escolha)

        assert resultado == esperado

    def teste_operacaoinvalida(self):
       #Recebe o valor 'ABCDE' e retorna 'ABCDE'
       
        entrada_n1 = 3
        entrada_n2 = 4
        entrada_escolha = 'Opa'
        esperado = 'Operação Invalida'
        resultado = calculadora(entrada_n1,entrada_n2,entrada_escolha)

        assert resultado == esperado

if __name__ == '__main__':
    unittest.main()