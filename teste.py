# Agora, vamos importar o nosso módulo de calculadora para este script:
import calc
#Solicitando valores ao usuário:
valor1 = input('digite um valor: ')
valor2 = input('digite outro valor: ')
#armazenando a soma:
soma = calc.somar(valor1, valor2)
#Exibindo a soma:
print('A soma é: {}'.format(soma))
#fazendo o mesmo com as outras funções do módulo:
divisao = calc.dividir(valor1, valor2)
print('A divisão é: {}'.format(divisao))
#Fazendo o mesmo colocando a chamada da função dentro do .format
print('A multiplicação é {}'.format(calc.multiplicar(valor1, valor2)))
# E outro jeito
subtracao = print('A subtração é {}'.format(calc.subtrair(valor1, valor2)))

#Podemos selecionar funções específicas do módulo com o comando "from":
#importação de funções específicas do módulo calc.py
from calc import somar, subtrair
#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = somar(valor1, valor2)
#exibindo a soma
print("A soma é {}".format(soma))
#E a subtração:
subtracao = print('A subtração é {}'.format(subtrair(valor1,valor2)))


