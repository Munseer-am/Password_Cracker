import hashlib

def Passwd_Cracker():
	hash = input('Enter md5 hash: ')
	f = open('rockyou.txt','rb')
	str = f.read()
	for word in str.split():
		s = word.decode("utf-8")
		enc = hashlib.md5(word).hexdigest()
		if enc == hash:
			print('\033[0;32mpassword found')
			print(f'\033[0;32mpassword is: {s}')
			quit()
		else:
			print(f'\033[0;31mpassword not found {s}')
			
Passwd_Cracker()
