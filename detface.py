import cv2 as cv
import os

# Função para busca de arquivos necessários do OpenCV 
def find(name, path):
    for root, dirs, files in os.walk(path):
        if (name in files) or (name in dirs):
            print("O diretorio/arquivo {} encontra-se em: {}".format(name, root))
            return os.path.join(root, name)
    # Caso nao encontre, voltar para diretorios anteriores
    return find(name, os.path.dirname(path))

# Importar arquivo XML
cvpath = os.path.dirname(cv.__file__)
haar_path = find('haarcascades', cvpath)
xml_name = 'haarcascade_frontalface_alt2.xml'
xml_path = os.path.join(haar_path, xml_name)

# TODO: Inicializar Classificador
clf = cv.CascadeClassifier(xml_path)

# Inicializar webcam
cap = cv.VideoCapture(0)

# Loop para leitura do conteúdo
while(not cv.waitKey(20) & 0xFF == ord('q')):
        # Capturar proximo frame
        ret, frame = cap.read()

        # TODO: Converter para tons de cinza
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # TODO: Classificar
        faces = clf.detectMultiScale(gray)

        # TODO: Desenhar retangulo
        for x, y, w, h in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0))

        # Visualizar
        cv.imshow('frame',frame)

# Desligar a webcam
cap.release()

#Fechar janela do vídeo
cv.destroyAllWindows()
cv.waitKey(1)
