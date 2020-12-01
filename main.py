import speech_recognition as sr
import pyttsx3
from random import choice
from config import *

reproducao = pyttsx3.init()

def repro(res):
    reproducao.say(res)
    reproducao.runAndWait()

def assistente():
    print("Qual seu nome completo?")
    repro("Qual seu nome completo?")
    while True: 
        res_erroA = choice(lista_erros)
        rec = sr.Recognizer()
        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)
            while True: 
                try:
                    audio = rec.listen(s)
                    user_name = rec.recognize_google(audio, language="pt-BR")
                    user_name = verifica_nome(user_name)
                    name_list()
                    apresentacao = "{}".format(verifica_nome_existe(user_name))
                    repro(apresentacao)
                    print(apresentacao)

                    brute_user_name = user_name
                    user_name = brute_user_name.split(" ")
                    user_name = user_name[0]
                    break
                except sr.UnknownValueError:
                    repro(res_erroA)
            break    

    print("=" * len(apresentacao))
    print("Ouvindo")

    while True: 
        res_erroA = choice(lista_erros)
        rec = sr.Recognizer()
        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)
            while True: 
                try:
                    audio = rec.listen(s)
                    entrada = rec.recognize_google(audio, language="pt-br")
                    print("{}: {}".format(user_name, entrada))
                    #Operações Matematicas:
                    if "Quanto é" in entrada:
                        entrada = entrada.replace("Quanto é","")
                        resposta = calcula(entrada)
                    #Clima/Tempo:
                    elif "Qual a temperatura" in entrada:
                        lista_tempo = temperatura()
                        temp = lista_tempo[0]
                        temp_max = lista_tempo[1]
                        temp_min = lista_tempo[2]
                        resposta = "A temperatura atual é de {}. A maxima é de {} e a minima é de {}".format(temp,temp_max,temp_min)
                    elif "informações da cidade" in entrada:
                        resposta = "Mostrando informações"
                    elif "desligar" in entrada:
                        repro("Encerrando")
                        print("Encerrando")
                        exit()
                    else:
                        resposta = conversa[entrada]

                    if resposta == "Mostrando informações":
                        lista_info = clima_tempo()  
                        long = lista_info[0]
                        lat = lista_info[1]
                        temp = lista_info[2]
                        pressaoatm = lista_info[3]
                        umidade = lista_info[4]
                        temp_max = lista_info[5]
                        temp_min = lista_info[6]
                        v_speed = lista_info[7]
                        direcao = lista_info[8]
                        neb = lista_info[9]
                        id_cidade = lista_info[10]

                        print("Assistente:")
                        print("Mostrando informações de {}".format(cidade))
                        repro("Mostrando informações de {}".format(cidade))
                        print("Longitude: {}".format(long))
                        print("Latitude: {}".format(lat))
                        print("Temperatura Atual: {:.2f}".format(temp))
                        print("Temperatura Maxima: {:.2f}".format(temp_max))
                        print("Temperatura Minima: {:.2f}".format(temp_min))
                        print("Pressão Atmosférica: {}".format(pressaoatm))
                        print("Umidade: {}".format(umidade))
                        print("Velocidade do Vento: {}".format(v_speed))
                        print("Direção do vento: {}m/s".format(direcao))
                        print("Nebulosidade: {}".format(neb))
                        print("ID da cidade: {}".format(id_cidade))
                    else:
                        print("Assistente: {}".format(resposta))
                        repro("{}".format(resposta))
                except sr.UnknownValueError:
                    repro(res_erroA)

if __name__ == '__main__':
    intro()
    repro("Iniciando")
    assistente()
