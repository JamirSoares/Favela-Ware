## Maria Eduarda e Emily Soares

from random import randint
import os
from pyfiglet import figlet_format
print(figlet_format('gerador de senha'))
print('GERADOR DE SENHAS EMILLY E MARIA \n')
listaMenu = ['1. Gerar Senha', '2. Desenvolvedores', '3. Sair']
while True:
    for i in range(len(listaMenu)):
        print(listaMenu[i])
    opcao = input('Escolha uma opcao:')
    print(opcao)

    if(opcao == '1'):
        os.system('cls')
        listaEspeciais = ['%','#','&','+','@','/','*','.','!','0','1','2','3','4','5','6','7','8','9','(',')','-','_','§','=','>','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        senha = ''
        for i in range (8):
            r=randint(0,len(listaEspeciais)-1)
            senha = senha + str(listaEspeciais[r])
        print(senha)
        
    elif (opcao == '2'):
        os.system('cls')
        print('Maria Eduarda','Emilly Soares')
    elif (opcao == '3'):
        os.system('cls')
        print('O programa sera fechado!')
        break
    else:
        print('Escolha uma da opcao:')