import psutil
import os
import time
import datetime



def vpn():

    psutil.process_iter()  
    lista = []
    file = open("pptp.txt" , "a")
    file.close()

    log = os.stat("pptp.txt")

    for proc in psutil.process_iter():
        lista.append(proc.name())

    
    if "pppd" in lista:
        
        if log.st_size > 3000:
            f = open("pptp.txt" , "w")
            f.write(datetime.datetime.now().ctime() + "  konektovano\n")
            f.close()
        else:
            f = open("pptp.txt" , "a")
            f.write(datetime.datetime.now().ctime() + "  konektovano\n")
            f.close()
    else:
        os.system("sudo pon pptp &")
        if log.st_size > 3000:
            f = open("pptp.txt" , "w")
            f.write(datetime.datetime.now().ctime() + "  Konekcija je pokusana\n")
            f.close()
        else:
            f = open("pptp.txt" , "a")
            f.write(datetime.datetime.now().ctime() + "  Konekcija je pokusana\n")
            f.close()
while True:

    vpn()
    time.sleep(10)