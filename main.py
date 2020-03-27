# -*- coding: utf-8 -*-
import os
import webbrowser
import argparse
from lib import whois
from lib import nmapScan
from lib import nikto
from lib import gobuster
from lib import enum4linux
from lib import show
from lib import dnsenum
from lib import theharvester
from time import sleep
import colorama
from colorama import Fore, Back, Style


class Main:
	def __init__(self):
		parse = self.parser()
		if not parse.url:
			print(Fore.RED+"enter url\nmain.py -u google.com")
		else:
			self.url = parse.url
			self.settings()
	def parser(self):
		parseObject = argparse.ArgumentParser()
		parseObject.add_argument("-u",dest="url", help="enter url")
		parse = parseObject.parse_args()
		return parse
	def settings(self):
		os.system("clear")
		try:
			#if your browser does not open this url. manually open your browser, paste this url on your browser and press enter. Be relax. This music is for you
			#Aktif et. Sana süprizim => bir alt satırdaki pass sil ve onun altındaki kodun başında olan "#" işareti sil
			pass
			#webbrowser.get('firefox').open_new_tab("https://www.youtube.com/embed/gYtybgToH2Q?autoplay=1&end=426&loop=1&start=26")
		except:
			pass
		show.giris()
		sleep(2)
		try:
			self.run()
		except:
			pass
	def run(self):
		print("\n   "+"*"*40,"\n","-"*20+"WHOİS"+"-"*20,"\n   "+"*"*40,"\n")
		whois.Whois(self.url)
		print("\n    "+"*"*40,"\n","-"*20+"DNSENUM"+"-"*19,"\n","   "+"*"*40,"\n")
		dnsenum.Dnsenum(self.url)
		print("\n      "+"*"*40,"\n","-"*20+"THEHARVESTER"+"-"*19,"\n","     "+"*"*40,"\n")
		theharvester.Theharvester(self.url)
		print("\n  "+"*"*40,"\n","-"*20+"NMAP"+"-"*20,"\n",Fore.CYAN+"NMAP SABIR İSTER. SAĞLIKLI SONUÇ İÇİN BEKLEYİN","\n","  "+"*"*40,"\n")
		nmapScan.Nmap(self.url)
		print("\n   "+"*"*40,"\n","-"*20+"NIKTO"+"-"*20,"\n   "+"*"*40,"\n")
		nikto.Nikto(self.url)
		print("\n    "+"*"*40,"\n","-"*20+"GOBUSTER"+"-"*19,"\n","   "+"*"*40,"\n")
		gobuster.Gobuster(self.url)
		print("\n      "+"*"*40,"\n","-"*20+"ENUM4LINUX"+"-"*19,"\n","     "+"*"*40,"\n")
		enum4linux.Enum(self.url)
		print(Fore.RED+"*"*50)
try:
	Main()
except KeyboardInterrupt:
	ex=0
	while (ex<=64):
		print(Fore.BLUE+"\r"+"#"*ex,end="")
		sleep(0.010)
		if ex == 64:
			print("\n")
		ex+=1
