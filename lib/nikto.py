# -*- coding: utf-8 -*-
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style

class Nikto(object):
	def __init__(self, url):
		colorama.init(autoreset=True)
		self.url = url
		self.nikto()
	def nikto(self):
		os.system("nikto -h "+self.url+" > 3.nikto.txt")
		with open("3.nikto.txt", "r", encoding="utf-8") as file:
			file = file.readlines()
			num = 0
			for i in file:
				if num % 2 == 0:
					print(Fore.YELLOW+i)
				else:
					print(Fore.BLUE+i)
				num += 1
		print(Fore.GREEN+'Rapor Yazdırıldı.')
		sleep(1)

		


