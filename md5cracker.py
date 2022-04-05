#!/usr/bin/python3
#!-- coding by Ali Qassem @e5t3hb4r47 --!#
import os,sys,hashlib,time
def decryption(hash,wordlist):
	try:
		if len(hash)!=32:
			print ("\033[1;31mThis hash is not MD5\033[0m")
			exit()
		if not os.path.isfile(wordlist):
			print ("\003[1;31mError No Such File \033[0m"+wordlist)
			sys.exit(2)
		loop = 1
		with open(wordlist,encoding='latin-1') as wl:
			for passwd in wl:
					passwd=passwd.replace("\n","")
					final=hashlib.md5(passwd.encode()).hexdigest()
					print ("\033[1;37m["+str(loop)+"]"+"\033[1;33m Trying this password : {}".format(passwd))
					if final==hash:
						time.sleep(3)
						print ("\033[1;32m[+] Decryption Successfully [+]\033[0m")
						print ("\033[1;33m"+hash+"\033[1;37m:\033[1;36m"+passwd)
						break
					else:
						print ("\033[1;31mInvalid"+":"+passwd)
					loop+=1
		print ("\033[1;33mCoded by @e5t3hb4r47\033[0m")
	except KeyboardInterrupt as key:
		print (key)
		sys.exit(1)
	except KeyError as keyer:
		print (keyer)
		sys.exit(1)
	except EOFError as error:
		print (error)
		sys.exit(1)
if len(sys.argv) !=3:
	print ("\033[1;37mUsage : md5cracker.py [hash] [wordlist]")
	sys.exit("\033[1;33mCoded by @e5t3hb4r47\033[0m")
decryption(sys.argv[1],sys.argv[2])
