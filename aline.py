#!/usr/bin/python
from time import sleep
from vosk import Model,KaldiRecognizer
import os
import core
import espeakng
import json
import pyaudio
import random
from train.classifier import classify

validate_loop = True
p = pyaudio.PyAudio()
    
model = Model('/home/luiz/Documents/aline/model/vosk-pt')
rec = KaldiRecognizer(model,16000)

list_hello = ["Olá Mr. luuiizz!","Oii!","Olá,pronto pro trabalho","vamos iniciar mais um dia","trabalhar né?","acordei","to aqui","que foooooi?","de novooooo!!!"]
list_welcome = ["Como sempre,memória ok e disco também","estou ótima","aqui e bem","pronta para trabalhar","vamos que vamos","atualizado e operante","vamos trabalhar"]

aline = espeakng.Speaker()
aline.wpm = 140
aline.pitch = 120
aline.voice = 'pt-br'


stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=2048)
stream.start_stream()

while validate_loop:

    data = stream.read(2048,exception_on_overflow = False)

    if(len(data) == 0):
        break

    if(rec.AcceptWaveform(data)):
        result = rec.Result()
        result = json.loads(result)

        if result is not None :
            text = result['text']
            text = text.lower().strip()
            print(text)
            if ('<UNK>' not in text) and  len(text) >= 3:
                entity = classify(text)
                print(text,entity)

                if entity == 'welcome\getWelcome':
                    mss = list_hello[random.randrange(len(list_hello))]
                    aline.say(mss)

                elif entity == 'up\getUp':
                    mss = list_welcome[random.randrange(len(list_welcome))]
                    aline.say(mss)

                elif entity == "jira\getJira":
                    aline.say("um minuto.")
                    core.SystemInfo.jira()
                    aline.say("Jira aberto,projetoos ok!")

                elif entity == 'system-manjaro\getUpdate' :
                    aline.say("um minuto...")
                    sleep(3) 
                    aline.say(core.SystemInfo.update_npm()) 
                    sleep(1)
                    aline.say(core.SystemInfo.update_pip())
                    sleep(1)
                    aline.say(core.SystemInfo.update_system())    
# 4556          
                elif entity == 'linkedin\getLinkedin':
                    aline.say("um minuto.....")
                    core.SystemInfo.linkedin()
                
                elif entity == 'message\getMessage':
                    aline.say("um minuto....")
                    core.SystemInfo.message()

                elif entity == 'temper\getTemper':
                    aline.say(core.SystemInfo.get_temper())

                elif entity == 'time\getTime':
                    aline.say(core.SystemInfo.get_time())

                elif entity == 'chrome\getChrome':
                    aline.say('Peraii chefe...')
                    os.system('google-chrome-stable')
                    sleep(3) 
                    aline.say("Navegadoor abertoo")
                
                elif entity == 'youtube\getYoutube':
                    aline.say("um minuto....")
                    core.SystemInfo.youtube()
                    aline.say("youtube aberto")

                elif entity == 'search\getSearch':
                    validate = True
                    aline.say('O que deseeja pesquisaar ?')

                    data = stream.close()

                    stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=2048)
                    stream.start_stream()

                    while validate :

                        data = stream.read(2048,exception_on_overflow = False)

                        if(rec.AcceptWaveform(data)):
                            result = rec.Result()
                            result = json.loads(result)

                            #print("pesquisado:" ,result)

                            if result is not None :
                                text = result['text']
                                text = text.lower().strip().replace('pesquisar','')
                                
                                if ('<UNK>' not in text) and  len(text) >= 3:
                                    print("pesquisando...")
                                    core.SystemInfo.search_google(text)
                                    validate = False
                                elif "sair" in text :
                                    validate = False

                    data = stream.close()
                    stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=2048)
                    stream.start_stream()
                
            else:
                print("entrada invalida!")

os.system("exit")
                  

            
            