import requests as rq

cidade = "porto+seguro"
version = "0.1.0"


def intro():
    msg = "Assistente - Versão {} | feito por: Jhonata Souza".format(version)
    print("-" * len(msg) + "\n{}\n".format(msg) + "-" * len(msg))

lista_erros = [
    "Não entendi nada",
    "Desculpe, não entendi",
    "Repita novamente, por favor"
] 

conversa = {
}

comandos = {
    "Desligar":"Encerrando",
    "Reiniciar": "Reinicializando"
}

def verifica_nome(user_name):
    if user_name.startswith("Meu nome é"):
        user_name = user_name.replace("Meu nome é", "")
    if user_name.startswith("Eu me chamo"):
        user_name = user_name.replace("Eu me chamo", "")
    if user_name.startswith("Eu sou o"):
        user_name = user_name.replace("Eu sou o", "")
    if user_name.startswith("Eu sou a"):
        user_name = user_name.replace("Eu sou a", "")
    return user_name

def verifica_nome_existe(nome):
    src = open("src/nomes.txt", "r")
    nome_list = src.readlines()

    if not nome_list:
        nullo = open("src/nomes.txt", "r")
        conteudo = nullo.readlines()
        conteudo.append("{}".format(nome))
        nullo = open("src/nomes.txt", "w")
        nullo.writelines(conteudo)
        nullo.close()

        return "Olá {}, prazer em conhece-lo.".format(nome)
    for linha in nome_list:
        if linha == nome:
            return "Olá {}, bem-vindo novamente, como posso ajuda-lo?".format(nome)
    
    nullo = open("src/nomes.txt", "r")
    conteudo = nullo.readlines()
    conteudo.append("\n{}".format(nome))
    nullo = open("src/nomes.txt", "w")
    nullo.writelines(conteudo)
    nullo.close()

    return "Oi {} bem-vindo, como posso ajuda-lo?".format(nome)

def name_list():
    try:
        nomes = open("src/nomes.txt", "r")
        nomes.close()
    except FileNotFoundError:
        nomes = open("src/nomes.txt","w")
        nomes.close()
    
def calcula(entrada):
    #Soma
    if "mais" in entrada or "+" in entrada:
        entradas_recebidas = entrada.split(" ")
        resultado = int(entradas_recebidas[1]) + int(entradas_recebidas[3])
    #Subtração
    elif "menos" in entrada or "-" in entrada:
        entradas_recebidas = entrada.split(" ")
        resultado = int(entradas_recebidas[1]) - int(entradas_recebidas[3])    
    #Multiplicação
    elif "vezes" in entrada or "x" in entrada:
        entradas_recebidas = entrada.split(" ")
        resultado = round(float(entradas_recebidas[1]) * float(entradas_recebidas[3]),10)
    #Divisão    
    elif "dividido" in entrada or "/" in entrada:
        entradas_recebidas = entrada.split(" ")
        resultado = round(float(entradas_recebidas[1]) / float(entradas_recebidas[3]),2)
    #Caso Não seja reconhecido a operação
    else:
        resultado = "Operação não encontrada"   

    return resultado

def clima_tempo():
    endereco_api = "http://api.openweathermap.org/data/2.5/weather?appid=3d6aa99be599cebcd4a6fa737de9c3cc&q="
    url = endereco_api + cidade
    #print(url)
    info =  rq.get(url).json()

    #Coordenadas
    long = info['coord']['lon']
    lat = info['coord']['lat']

    #Principal
    temp = info['main']['temp'] - 273.15
    pressaoatm = info['main']['pressure'] / 1013.25
    umidade = info['main']['humidity']
    temp_max = info['main']['temp_max'] - 273.15
    temp_min = info['main']['temp_min'] - 273.15

    #Vento
    v_speed = info['wind']['speed']
    direcao =  info['wind']['deg']
    
    #Nuvens

    neb = info['clouds']['all']

    #Cidade - ID

    id_cidade = info['id']

    return [long, lat, temp, pressaoatm, umidade, temp_max, temp_min, v_speed, direcao, neb, id_cidade,cidade]

def temperatura():
    temp_atual = clima_tempo()[2]
    temp_max = clima_tempo()[5]
    temp_min = clima_tempo()[6]
    return [temp_atual, temp_max, temp_min]