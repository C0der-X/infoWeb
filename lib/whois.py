# -*- coding: utf-8 -*-
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style
try:
	class Whois(object):
		def __init__(self, url):
			colorama.init(autoreset=True)
			self.url = url
			self.whois()
		def whois(self):
			os.system(f"whois {self.url} > 1.whois.txt")
			with open("1.whois.txt", "r", encoding="utf-8") as file:
				file = file.readlines()
				for i in file:
						print(Fore.WHITE+i)
			print(Fore.GREEN+"[+] Rapor Yazdırıldı.")
			sleep(1)
except:
	pass