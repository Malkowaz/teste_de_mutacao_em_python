# Codigo para testeeee YEEEEEEEEEY
'''
print("---------------------------------")
print("          Calculadora")
print("---------------------------------")
n1 = float(input('Digite o primeiro número: '))
print("---------------------------------")
n2 = float(input('Digite o segundo número: '))
print("---------------------------------")
print("      Escolha a operação:")
print("---------------------------------")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("---------------------------------")
escolha = input('Digite a operação: ')

print("---------------------------------")
'''
def calculadora(n1,n2,escolha):

    if escolha == '1':
        print(f'O Resultado foi: {n1 + n2}')
        return n1 + n2
    
    if escolha == '2':
        print(f'O Resultado foi: {n1 - n2}')
        return n1 - n2

    if escolha == '3':
        print(f'O Resultado foi: {n1 * n2}')
        return n1 * n2

    if escolha == '4':
        print(f'O Resultado foi: {n1 / n2}')
        return n1 / n2
    
    else:
        print('Operação Invalida')
        return 'Operação Invalida'

#calculadora(n1,n2,escolha)