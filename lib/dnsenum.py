# -*- coding: utf-8 -*-
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style

class Dnsenum(object):
	def __init__(self, url):
		colorama.init(autoreset=True)
		self.url = url
		self.dnsenum()
	def dnsenum(self):
		os.system("dnsenum "+self.url+" -o 6.dnsenum.txt")
		print(Fore.GREEN+'Rapor Yazdırıldı.')
		sleep(1)

		


