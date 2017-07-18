#coding utf8
#utf9_to_utf8.py
import utf9

utf9_file = open('1','rb')
utf_data = utf9_file.read()
decoded_data = utf9.utf9decode(utf_data)
print decoded_data
decoded_file = open('decoded','w')
decoded_file.write(decoded_data)
decoded_file.close()