import time
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
def giris():
	color=["Fore.GREEN+","Fore.RED+","Fore.YELLOW+"]
	a2=("""                                     
	 _____ ___ ____  ___ _____     __ __ 
	|     |   |    \\|_  | __  |___|  |  |
	|   --| | |  |  |_  |    -|___|-   -|   ___
	|_____|___|____/|___|__|__|   |__|__|      |
	                                           V              
				   	          ...      
					         (o -)     
					     ooO--(_)--Ooo-
		""")
	a3=("""
	 __  __  __  __  __         
	/   /  \\|  \\  _)|__) __ \\_/ 
	\\__ \\__/|__/ __)| \\     / \\ 
	                            
		""")
	a4color=Fore.RED+"~~~~~ Sağlam Hack, Sağlam Bilgide Bulunur ;) ~~~~~"
	a4=(f"""
		+-+-+-+-+-+-+-+
		|C|0|D|3|R|-|X|
		+-+-+-+-+-+-+-+
{a4color}
		""")
	rang=random.randint(0,23)
	if rang%3==0 or rang%7==0:
		print(Fore.CYAN+a2)
		time.sleep(1)
		ex=0
		while (ex<=64):
			print(Fore.BLUE+"\r"+"#"*ex,end="")
			time.sleep(0.010)
			if ex == 64:
				print("\n")
			ex+=1
	elif rang%5==0 or rang%11==0:
		print(Fore.YELLOW+a3)
		time.sleep(1)
		ex=0
		while (ex<=64):
			print(Fore.BLUE+"\r"+"#"*ex,end="")
			time.sleep(0.010)
			if ex == 64:
				print("\n")
			ex+=1
	else:
		print(Fore.GREEN+a4)
		time.sleep(1)
		ex=0
		while (ex<=64):
			print(Fore.BLUE+"\r"+"#"*ex,end="")
			time.sleep(0.010)
			if ex == 64:
				print("\n")
			ex+=1
