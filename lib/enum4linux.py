# -*- coding: utf-8 -*-
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style

class Enum(object):
	def __init__(self, url):
		colorama.init(autoreset=True)
		self.url = url
		self.enum4()
	def enum4(self):
		os.system(f"enum4linux {self.url} > 5.enum4.txt")
		with open("5.enum4.txt", "r", encoding="utf-8") as file:
			file = file.readlines()
			for i in file:
				print(Fore.YELLOW+i)
				
		print(Fore.GREEN+"Rapor Yazdırıldı.")
		sleep(1)