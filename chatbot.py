import webbrowser
import pyttsx3
from pyfiglet import *
from webbrowser import *
import os,subprocess

import speech_recognition as sr
#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    #usando o microfone
    with sr.Microphone() as source:
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        #Retorna a frase pronunciada
        #print("Você disse: " + frase)
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
    return frase
def fala (data):
    s = pyttsx3. init()
    s.say(data)
    print(data)
    s.runAndWait()
def inicio (data):
    s = pyttsx3. init()
    s.say(data)
    s.runAndWait()
''
fala('Olá!!, Bem vindo!! Meu nome é ')
texto = "SCARLET"
inicio(texto)
print(figlet_format(texto))
fala('Qual o seu nome ?')
comando = ouvir_microfone()
nome = comando
def processar_resposta (resposta,nome) :
    if resposta == '1':
        pass
def resposta(a):
    if a == '1':
        resposta = ('Na minha visão vale muito apena, isso porque Python é uma das linguagens que mais cresce no mundo e possui salários mensais que vão desde R$2100,00 a até mais R$10000,00 no Brasil, além de contar com uma média anual de $85.000 dolares nos EUA.')
    elif a == '2':
        resposta = (' Isso varia muito com o nível de esforço, dedicação e busca diária por vagas de cada indivíduo. Alguns conseguem com menos de 3 meses e outros com mais, tudo depende do quanto você já sabe ou está disposto a correr atrás para aprender.')
    elif a == '3':
        resposta = (' Primeiro entenda, ninguém vai te dizer ou chegar magicamente um dia e te dizer que você está BOM o suficiente para conseguir um emprego ou fazer dinheiro com seu conhecimento de programação, seja em Python ou qualquer outra linguagem ou habilidade, você simplesmente tem que começar dar a sua cara a tapa e começar a aplicar para oportunidades ou até mesmo começar a criar elas, desde o dia que você já domina os fundamentos de uma linguagem(se estamos falando de Python, recomendo aprender no mínimo os 5 pilares de programação.')
    elif a == '4':
        resposta = ('você pode estudar através de vídeos gratúitos no YouTube, livros e sites de programação, porém se buscar um lugar com suporte 1 a 1, estrutura sequencial, projetos novos todos os meses dos ano e um curso que vai te ensinar toda a base e habilidades mais lucrativas que precisa para criar aplicações em python e estar pronto para o mercado.')
    elif a == '5':
        resposta = 'Qual site você quer abrir?'
        fala(resposta)
        comando = ouvir_microfone()
        pesquisa = str(comando) + '.com'
        webbrowser.open(str(pesquisa))
        print(comando)
    fala(resposta)
    comando = ouvir_microfone()
    

def menu(nome):
    resposta = 'Oque você gostaria de aprender hoje sobre python ?' + str(nome) +' \n[1] - Vale apena aprender python ?\n[2] - Quanto tempo leva para conseguir um emprego com python?\n[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego ?\n[4] - Onde me recomenda estudar python para conseguir um emprego hoje ?\n [5] Ou abrir programa '
    fala(resposta)
    comando = ouvir_microfone()
    return comando

start = menu(nome)
resposta(start)


