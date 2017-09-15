def xor(key, string):
	result = ''
	for i in range(len(string)):
		result += chr(ord(string[i]) ^ ord(key[i%len(key)]))
	return result

def rotate(key):
	initkey = key
	lst = []
	while True:
		newkey = key[1:] + key[0]
		lst.append(newkey)
		if newkey == initkey:
			break
		key = newkey
	return lst
	
if __name__ == "__main__":
	initkey = '(g)(&m4fgfj#^d@A%32F3!BV54g#12h*'
	string = "HEQdUDsHMiRREQhkfmAKGXZ8Jm12cSdkYCJnfmkkei4mMydsFycICGBmEGoRVDEzR1oGTlQQUghJBkhJRwxVBwYHC0I/BSEgRFJTJ1JAIzdUVQZCUFMJS0kGSElHDFUHBgcLQj8FISBEUhBqEVInNUdREwELED5jcCJhbXI1dSggLit6ECMVDmxncw52dRsTYBYa".decode('base64')
	lst = rotate(initkey)
	for key in lst:
		if "username" in xor(key,string):
			print xor(key,string)
			print key