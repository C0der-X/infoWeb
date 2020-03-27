# -*- coding: utf-8 -*-
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style

class Gobuster(object):
	def __init__(self, url):
		colorama.init(autoreset=True)
		self.url = url
		self.wordlistFiles='/usr/share/dirb/wordlists/common.txt'
		self.goBust()
	def goBust(self):
		os.system(f"gobuster dir -u {self.url} -w {self.wordlistFiles} > 4.goBuster.txt")
		with open("4.goBuster.txt", "r", encoding="utf-8") as file:
			file = file.readlines()
			num = 0
			for i in file:
				if num % 2 == 0:
					if i[0] == "/":
						print(Fore.YELLOW+("http://" + self.url + i))
					else:
						print(Fore.YELLOW+i)
				else:
					if i[0] == "/":
						print(Fore.GREEN+("http://" + self.url + i))
					else:
						print(Fore.GREEN+i)
				num += 1
		print(Fore.GREEN+"[+] Rapor Yazdırıldı.")
		sleep(1)