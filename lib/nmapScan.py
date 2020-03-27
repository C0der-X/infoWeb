# -*- coding: utf-8 -*-
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style

class Nmap(object):
	def __init__(self, url):
		colorama.init(autoreset=True)
		self.url=url
		self.scan()
	def scan(self):
		os.system(f'nmap -Pn -sS -sV -n -p- -T4 {self.url} -oN 2.nmap.txt')
		print(Fore.GREEN+"Rapor Yazdırıldı.")
		sleep(1)
