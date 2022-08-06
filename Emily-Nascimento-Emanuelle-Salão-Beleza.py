## by Emanuelle Emilly Nascimento
## variaveis
from pyfiglet import *
print(figlet_format('salao'))
## VARIAVEIS
listaSalao=['1. Escova ','2.Corte de cabelo','3.Unha da mao ou pe','4.Pintar Cabelo','5.Cancelamento do cervico']
listaHorario=['1. 07:00','2. 08:30:','3. 09:30','4. 10:30']
servicoEscolhido = ''
horarioEscolhido = ''
erro = 0
listaAtendente=['1. Emily','2. Emanuelle','3. Jamir','4. Juliano']
## codigo inicio
while True:
    # for para rodar opcoes de servicos do salao
    for i in range(0,len(listaSalao)):
        print(listaSalao[i])   
    salao=input('escolha uma opção \n')

    # Escova
    if (int(salao)==1):
       servicoEscolhido='Escova'
    elif (int(salao)==2):
        servicoEscolhido='Corte de cabelo'
    elif (int(salao)==3):
         servicoEscolhido='unha da mao ou do pe'
    elif (int(salao)==4):
        servicoEscolhido='Pitar cabelo'
    elif (int(salao)==5):
        break
    else:
        print('servico invalido')
        servicoEscolhido='Cancelamento'

    #agendamento de horario
    print('agende seu horario')
    print('Horarios disponiveis:')
    
    # for para rodar opcoes de horarios do salao
    for i in range(0,len(listaHorario)):
        print(listaHorario[i])
    horario=str(input('escolha um horario \n')) 

    # 07:00
    if(int(horario)==1):
        horarioEscolhido='07:00'
        atendenteEscolhida='Emily'
        break
    #08:30
    elif(int(horario)==2):
        horarioEscolhido='08:30'
        atendenteEscolhida='Emanuelle'
        break
    #09:30
    elif(int(horario)==3):
        horarioEscolhido='09:30'
        atendenteEscolhida='Jamir'
        break
    #10:30
    elif(int(horario)==4):
       horarioEscolhido='10:30'
       atendenteEscolhida='Juliano'  
       break
    else:
        print('horario invalido')

print('AGENDAMENTO')     
print('Servico Escolhido ' + str(servicoEscolhido))
print('Horario Escolhido ' + str(horarioEscolhido))
print('Atendente Escolhido ' + str(atendenteEscolhida))
print('AVALIE O APLICATIVO ATE 5 ESTRELAS')
avaliaçao=str(input())
print('OBRIGADO POR AVALIAR!')


  