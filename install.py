import os


def python():
    os.system("sudo apt-get update")
    os.system("sudo apt-get install omxplayer -y")
    os.system("sudo apt-get install git -y")
    os.system("sudo apt-get install python-pip -y")
    os.system("pip install psutil")

python()
