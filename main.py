"""
this code is protected under the MIT License (MIT)
Ben Kreger GlomCo 2013

"""
import ftplib 
from ftplib import FTP
import os
import sys
import getpass
import random
import math 
import random
import time
def cauchy(location, scale): #I got these from a website, give credit to the programmers not me.
    p = 0.0
    while p == 0.0:
        p = random.random()
        
    return location + scale*math.tan(math.pi*(p - 0.5))

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
prev = 00#From here on this is my code
ftp = FTP(host, username, password)
    #ftp.login()
ftp.cwd("/Bencoin/")
print "Ben Coin by Ben Kreger 2013)"
#text = text.replace('Q', '1')
#print"Your name is:"
name = getpass.getpass('Password:')
file23 = ftp.nlst()
    #if file23.find("" + s) == -1:
name1 = name + ".dat"
if any(ext in name1 for ext in file23):
    print "getting amount"
    fillo = name1
    lf = open(name1, "wb")
    ftp.retrbinary("RETR " + fillo, lf.write, 8*1024)
    lf.close()
else:
    print "Error ask Ben to add your name"
    sys.exit()
name6 = name + ".key"
if any(ext in name6 for ext in file23):
    print "getting key"
    fillo = name6
    lf = open(name6, "wb")
    ftp.retrbinary("RETR " + fillo, lf.write, 8*1024)
    lf.close()
    file = open(name6, 'r')
    key = file.read()
    file.close()
else:
    print "Error ask Ben to add a key for your name"
    sys.exit()
file = open(name1, 'r')
text = file.read()
print text
#print"Your name is:",
#print name
print "Your key is",
print key

print"""
    ____  ______ _   _  _____ ____ _____ _   _ 
   |  _ \|  ____| \ | |/ ____/ __ \_   _| \ | |
   | |_) | |__  |  \| | |   | |  | || | |  \| |
[::::::::::::::::::::::::::::::::::::::::::::::::]
   | |_) | |____| |\  | |___| |__| || |_| |\  |
   |____/|______|_| \_|\_____\____/_____|_| \_|
                                             
"""
		
text = int(text)
file.close()
print "Balance:    "
print text,
print "BEN"
print"""
(1) Give BenCoin
(2) Receive BenCoin
(3) Mine Bencoin
"""
while(True):
    while(True):
        upload(ftp, name1)
        file = open(name1, 'r')
        text1111 = file.read()
        print"You have",
        print text1111,
        print"BenCoin"
        file.close()
        ch = raw_input(">>")
        
        if(ch == "1"):
                if text < 20:
                    print"You are out of bencoins. "
                    break;
                num = input("How much Bencoin do you want to give? ")
                text = text - num
                print"New amount is: ",
                print text
                myfile = open(name1, "w")
                myfile.write(str(text))
                myfile.close()
                #print text
                who = raw_input("Other person's key")
                file22 = ftp.nlst()
                if any(ext in who for ext in file22):
                    lf = open("buffer", "wb")
                    ftp.retrbinary("RETR " + who, lf.write, 8*1024)
               # print numfo
                    lf.close()
                    lf = open("buffer", "r")
                    whe = lf.read()
               # print numfo
                    lf.close()
                myfile = open(who, "w")
                myfile.write(str(num + int(whe)))
                myfile.close()
                upload(ftp, who)
                
            
        if(ch == "2"):
            file22 = ftp.nlst()
            if any(ext in key for ext in file22):
                fillo = key#raw_input("File")
                lf = open("suchben.dll", "wb")
                ftp.retrbinary("RETR " + fillo, lf.write, 8*1024)
                lf.close()
                lf = open("suchben.dll", "r")
                text11 = lf.read()
                print text11,
                print "BenCoin found."
                text = text + int(text11)
                print text
                myfile = open(name1, "w")
                myfile.write(str(text))
                myfile.close()
                ftp.delete(fillo)
                text11 = int(text11)
                #print text
                lf.close()
            else:
                print"No Bencoin found"
        if(ch == "3"):
            trys = 0
            while True:
                trys = trys + 1
                cake1 = round(cauchy(1, 999999))#abs(x)
                if(cake1 < 0):
                    cake1 = cake1 * -1
                print trys,
                print":   ",
                print cake1
                print "de"
                #cake1 = -4305887445.0
                if(cake1 == 643276):
                    #raw_input("")
                    file = open(name1, 'w')
                    text1111 = int(text1111) + 1
                    file.write(str(text1111))
                    print"You have",
                    print text1111,
                    print"BenCoin"
                    file.close()
		    file = open("LOG.txt", 'a')
                    file.write(time.strftime("%I:%M:%S"))
                    file.close()
                    upload(ftp, name1)
                    #raw_input("")
        
