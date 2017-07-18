# -*- coding: utf-8 -*-
#vigenereDictionaryHacker.py
import detectEnglish
 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
def translateMessage(key, message, mode):
    translated = [] # 存储加密/解密消息字符串
    keyIndex = 0
    key = key.upper()
    for symbol in message: # 遍历每个消息里的字符的消息
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 意味着转换为大写在LETTERS找不到
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # 加密时相加
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # 解密时相减
            num %= len(LETTERS) # 处理潜在的循环           
            # 添加转换后加密/解密字符
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1 # 继续下一个用密钥字符来解密
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # 字符不在LETTERS里直接添加
            translated.append(symbol)
    return ''.join(translated)
 
def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')
 
def hackVigenere(ciphertext):
    fo = open('keys.txt')
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip()
        decryptedText = decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            print('------------------------>>>Notice!<<<----------------------')
            print('Possible encryption break:')
            print('->>Possible key: ' + str(word))
            print('->>Possible plaintext: ' + decryptedText[:100])
            print('Enter D for done, or just press Enter to continue breaking:')
            response = raw_input('> ')
            if response.upper().startswith('D'):
                return decryptedText
 
def main():
    ciphertext = """rla xymijgpf ppsoto wq u nncwel ff tfqlgnxwzz sgnlwduzmy vcyg ib bhfbe u tnaxua ff satzmpibf vszqen eyvlatq cnzhk dk hfy mnciuzj ou s yygusfp bl dq e okcvpa hmsz vi wdimyfqqjqubzc hmpmbgxifbgi qs lciyaktb jf clntkspy drywuz wucfm"""
    hackedMessage = hackVigenere(ciphertext)
    if hackedMessage != None:
        print('\nCopy Possible plaintext to the clipboard:\n')
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')
 
if __name__ == '__main__':
    main()
