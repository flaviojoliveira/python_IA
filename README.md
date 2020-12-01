# Assistente Virtual

Nesse projeto, nós criamos uma assistente virtual utilizando a linguagem de programação [Python](https://www.python.org/) e algumas bibliotecas para a que seja possível a realização de algumas tarefas utilizando Reconhecimento de Fala.

## Requisitos

 - Python 3+
 - Microfone

## Instalação

Utilizando um terminal, instale as seguintes bibliotecas utilizando o pip:

```pip3 install SpeechRecogniton```

```pip3 install PyAudio```

```pip3 install pyttsx3```

Caso esteja utilizando Linux e dê o seguinte erro: 

`libespeak.so.1: cannot open shared object file: No such file or directory`

instale o seguinte pacote: 

 - Arch linux e derivados:

    ```sudo pacman -S espeak```

 - Ubuntu e derivados:

    ```sudo apt-get install espeak```

## Execução

Após a instalação das dependecias utilizando o terminal entre na pasta aonde está localizada os arquivos e execute o seguinte comando:

```python main.py```

## Exemplo:

[Video](https://youtu.be/RnoQmsoNB9Q)


