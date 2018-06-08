'''
import urllib 
import urllib.request
print ("downloading with urllib")
url = 'http://api.bitcoincharts.com/v1/csv/'
print ("downloading with urllib")
path =r'C:\Users\dell\Desktop\new.csv'
urllib.request .urlretrieve(url, path)
print("finish")
'''
#!/usr/bin/python 
# -*- coding:utf-8 -*- 
  
import urllib              #导入urllib模块 
import urllib2             #导入urllib2模块 
import re               #导入正则表达式模块：re模块 
  
def getPDFFromNet(inputURL): 
  req = urllib2.Request(inputURL) 
  f = urllib2.urlopen(req)         #打开网页 
  localDir = 'E:\downloadCSV\\'        #下载CSV文件需要存储在本地的文件夹 
  urlList = []            #用来存储提取的CSV下载的url的列表 
  for eachLine in f:          #遍历网页的每一行 
    line = eachLine.strip()       #去除行首位的空格，习惯性写法 
    if re.match('.*csc.gz*', line):      #去匹配含有“cec.gz”字符串的行，只有这些行才有PDF下载地址 
      wordList = line.split('\"')    #以"为分界，将该行分开，这样就将url地址单独分开了 
      for word in wordList:      #遍历每个字符串 
        if re.match('.*\.csv.gz$', word): #去匹配含有“.csv.gz”的字符串，只有url中才有 
          urlList.append(word)  #将提取的url存入列表 
  for everyURL in urlList:         #遍历列表的每一项，即每一个CSV的url 
    wordItems = everyURL.split('/')     #将url以/为界进行划分，为了提取该PDF文件名 
    for item in wordItems:       #遍历每个字符串 
      if re.match('.*\.csv.gz$', item):   #查找CSV的文件名 
        PDFName = item     #查找到PDF文件名 
    localPDF = localDir + PDFName      #将本地存储目录和需要提取的PDF文件名进行连接 
    try:            
      urllib.urlretrieve(everyURL, localPDF) #按照url进行下载，并以其文件名存储到本地目录 
    except Exception,e: 
      continue
  
getPDFFromNet('http://api.bitcoincharts.com/v1/csv/')
print "finish"
