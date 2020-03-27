# -*- coding: utf-8 -*-
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style

try:
	class Theharvester(object):
		def __init__(self, url):
			colorama.init(autoreset=True)
			self.url = url
			self.theHarvester()
		def theHarvester(self):
			
			os.system("theHarvester -d "+self.url+" -l 500 -b bing,google,hunter,linkedin,twitter,yahoo,vhost,dnsdumpster -f 7.theHarvester")

			print(Fore.GREEN+'Rapor Yazdırıldı.')
			sleep(1)

except:
	pass		


