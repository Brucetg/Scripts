import zipfile

def bruteZipPass(zfile,path,password):
	try:
		zfile.extractall(path=path,pwd = password)
		return True
	except:
		return False

def zipCrack(filename):
	with zipfile.ZipFile(filename) as zfile:
		for p in range(99999):
			if bruteZipPass(zfile,'./',str(p)):
				print 'success',p
				return zfile.namelist()[0]

if __name__ == '__main__':
	filename = '13812.zip'
	try:
		while 1:
			filename = zipCrack(filename)
	except:
		print 'zipcrack finish'
		print 'filename:',filename
