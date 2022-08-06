## by Yuri e Leticia
from pyfiglet import *
import math
print(figlet_format('calculadora'))
listaOperacoes = ['soma','sub','div','mult','raiz', 'elevado','sair']
operacao = input("digite a operacao desejada: ").lower()
if operacao != "raiz":
    numero1 = input('digite o primeiro numero:')
    numero2 = input('digite o segundo numero:')
else:
    numero = int (input ('digite o numero'))
if operacao == 'soma':
    resultado = float (numero1) + int(numero2)
elif operacao == "sub":
    resultado = float(numero1) - int (numero2)
elif operacao == "div":
    resultado = float (numero1) / int (numero2)
elif operacao == "mult":
    resultado = float (numero1) * int (numero2)
elif operacao == "raiz":
    
    resultado = float(math.sqrt(numero))
elif operacao == "elevado":
    resultado = float (numero1) ** int (numero2)
else:
    resultado = "operação nao suportada"
print ('o resultado da operação é: ' + str (resultado))
input()