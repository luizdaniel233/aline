import datetime
import requests
import webbrowser
import os

lat = "3.1316333"
lon = "-59.9825041"
API_KEY = "2385866f1f825a1e4f0025ac6ca40a3b"
city = "manaus"
link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=pt-br"


class SystemInfo :

    def __init__(self):
        pass

    @staticmethod
    def update_system():
        os.system("sudo pacman -Syu")
        return "...pacotes atualizados"

    @staticmethod
    def jira():
        webbrowser.open_new("https://ghostmarket.atlassian.net/jira/software/projects/META/boards/95/backlog")
        webbrowser.open_new("https://ghostmarket.atlassian.net/jira/software/projects/META/boards/96/backlog")
        webbrowser.open_new("https://ghostmarket.atlassian.net/jira/software/projects/ZOOT/boards/89/backlog")

    @staticmethod
    def update_pip():
        os.system("python3 -m pip install --upgrade pip")
        return "...pip atualizado!"
    
    @staticmethod
    def update_npm():
        os.system("npm install -g npm@latest")
        return "...npm atualizado!"

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos'.format(now.hour,now.minute)
        return answer

    @staticmethod
    def get_temper():
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        temperatura = requisicao_dic['main']['temp'] - 273.15
        return f"{int(temperatura)} graus celcius"

    @staticmethod
    def search_google(search):
        webbrowser.open_new(f'https://www.google.com/search?q={search}')
    
    @staticmethod
    def youtube():
        webbrowser.open_new("https://www.youtube.com/")

    @staticmethod
    def linkedin():
        webbrowser.open_new("https://www.linkedin.com/in/luiz-daniel-ba1519199/")
    
    @staticmethod
    def message():
        try :
            webbrowser.open_new("https://outlook.office.com/mail/")
            webbrowser.open_new("https://web.whatsapp.com/")
            webbrowser.open_new('https://mail.google.com/mail/u/0/#inbox')
            webbrowser.open_new('https://mail.google.com/mail/u/1/#inbox')
        except webbrowser.Error as e:
            print(e)

        

