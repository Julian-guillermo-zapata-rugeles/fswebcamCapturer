"""
fotographic report using  fswebcam
Avalible on GNU/LINUX


Julian Guillermo Zapata Rugeles
"""
import os
import time

#------------------IMPORTANT----------------------
"""
esta sección contiene valores importates para la operacion del programa
por ejemplo minimal (representa la cantidad de imagenes a tomar de manera repetitiva)
mientras interval es el periodo que tardará entre cada imagen tomada



this section contains important values to program operation
example: minimal is how many pictures will be take by the program
and interval is the period using by the program between each taken pictures.

"""
minimal=13 # CHANGE THIS VALUE TO N PICTURES #
interval=2   # CHANGE THIS VALUE TO N INTERVAL
#-------------------------------------------------

pwd=os.popen("pwd").read()
pwd=pwd[:-1]
pwd=pwd+"/instants/"
createFolder="mkdir "+pwd+" 2>> /dev/null"
comandtoTakePicture="fswebcam -d /dev/video0 -r 640x480 --jpeg 100 -F 15 - > "+pwd
os.system(createFolder) #createFolder if don't exist



class observador():
    def takePictures(comando1,minimal,interval):
        cero=0
        while cero < minimal:
            date=os.popen("date").read()
            date=date.replace(" ","") ; date=date[:-1]
            comando=comando1+date+".jpg"
            os.system(comando)
            time.sleep(interval)
            cero=cero+1

    def detectIntall():
        # if packcage is installed , next
        # not : try to install using apt
        status=os.popen("dpkg -s fswebcam").read()
        if "install ok installed" in status:
            print("fswebcam installed ... Next ")
        else:
            print("no found fswebcam ...installing")
            os.system("sudo apt-get install fswebcam")
        print("validation pass")


if __name__ == '__main__':
    os.system("pkill fswebcam")
    os.system("clear")
    print("###################################")
    print("Programa iniciado con los valores ")
    print("Numero de capturas = ",minimal)
    print("Segundos entre captura ",interval)
    print("###################################")
    print("Tiempo estimado para la operacion :")
    estimate=(minimal*interval+(minimal*1.2))/60
    print("Aproximadamente ",estimate, "Minutos ")
    time.sleep(10)
    observador.detectIntall()
    observador.takePictures(comandtoTakePicture,minimal,interval)
    #Add your own process like compress Folder , Send to email , delete if folder size >N etc...
