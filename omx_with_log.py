import psutil
import datetime
import time
import os


def omx():
    lista = []

    for proc in psutil.process_iter():
        lista.append(proc.name())
    daLiPostojiLog = os.path.isfile("log.txt")
    if daLiPostojiLog == False:
        f = open("log.txt" , "w")
        f.write("")
        f.close()
    if "omxplayer.bin" in lista:
        proveraVelicine = os.stat("log.txt")
        if proveraVelicine.st_size < 2000:
            log = open("log.txt" , "a")
            log.write(datetime.datetime.now().ctime() + "    Proces vec postoji\n")
            log.close()
        else:
            log = open("log.txt" , "w")
            log.write(datetime.datetime.now().ctime() + "    Proces vec postoji\n")
            log.close()
    else:
        os.system("omxplayer -o hdmi --loop /home/pi/video.mp4 &")
        proveraVelicine = os.stat("log.txt")
        if proveraVelicine.st_size < 2000:
            log = open("log.txt" , "a")
            log.write(datetime.datetime.now().ctime() + "    Proces je pokrenut\n")
            log.close()
        else:
            log = open("log.txt" , "w")
            log.write(datetime.datetime.now().ctime() + "    Proces je pokrenut\n")
            log.close()

    f = open("logproces.txt" , "w")
    f.write("\n".join(lista))
    f.close()
    

while True:
    #os.system('omxplayer -o hdmi --loop /home/pi/video.mp4 &')
    omx()
    time.sleep(6)
    
