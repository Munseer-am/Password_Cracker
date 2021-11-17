import hashlib

def Passwd_Cracker():
        	print("""  \033[1;34;40m__  __
 |  \/  |_   _ _ __  ___  ___  ___ _ __
 | |\/| | | | | '_ \/ __|/ _ \/ _ \ '__|
 | |  | | |_| | | | \__ \  __/  __/ |
 |_|  |_|\__,_|_| |_|___/\___|\___|_|""")
	hash = input('Enter md5 hash: ')
	f = open('rockyou.txt','rb')
	str = f.read()
	for word in str.split():
		s = word.decode("utf-8")
		enc = hashlib.md5(word.encode()).hexdigest()
		if enc == hash:
			print('\033[0;32mpassword found')
			print(f'\033[0;32mpassword is: {s}')
			quit()
		else:
			print(f'\033[0;31mpassword not found {s}')
			
Passwd_Cracker()
