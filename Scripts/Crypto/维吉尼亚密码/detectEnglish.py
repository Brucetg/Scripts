# -*- coding: utf-8 -*-
# detectEnglish.py
# 英文单词探测模块
# 模块引用:
#   import detectEnglish
#   detectEnglish.isEnglish(someString) # 返回真或假
# 模块需要一个包含常见英文单词的"words.txt"，下载地址：http://invpy.com/dictionary.txt
 
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
 
def loadDictionary():
    dictionaryFile = open('words.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords
 
ENGLISH_WORDS = loadDictionary()
 
def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    # print possibleWords
    if possibleWords == []:
        return 0.0 # 没有单词返回0.0
 
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)
 
def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)
 
def isEnglish(message, wordPercentage=20, letterPercentage=85):
    # 默认设置转换后的message中单词的20%能在words.txt中的单词列表找到
    # 默认设置转换后的message中85%是字母或空格
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
