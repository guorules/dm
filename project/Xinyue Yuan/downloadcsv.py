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
  
import urllib              #����urllibģ�� 
import urllib2             #����urllib2ģ�� 
import re               #����������ʽģ�飺reģ�� 
  
def getPDFFromNet(inputURL): 
  req = urllib2.Request(inputURL) 
  f = urllib2.urlopen(req)         #����ҳ 
  localDir = 'E:\downloadCSV\\'        #����CSV�ļ���Ҫ�洢�ڱ��ص��ļ��� 
  urlList = []            #�����洢��ȡ��CSV���ص�url���б� 
  for eachLine in f:          #������ҳ��ÿһ�� 
    line = eachLine.strip()       #ȥ������λ�Ŀո�ϰ����д�� 
    if re.match('.*csc.gz*', line):      #ȥƥ�京�С�cec.gz���ַ������У�ֻ����Щ�в���PDF���ص�ַ 
      wordList = line.split('\"')    #��"Ϊ�ֽ磬�����зֿ��������ͽ�url��ַ�����ֿ��� 
      for word in wordList:      #����ÿ���ַ��� 
        if re.match('.*\.csv.gz$', word): #ȥƥ�京�С�.csv.gz�����ַ�����ֻ��url�в��� 
          urlList.append(word)  #����ȡ��url�����б� 
  for everyURL in urlList:         #�����б��ÿһ���ÿһ��CSV��url 
    wordItems = everyURL.split('/')     #��url��/Ϊ����л��֣�Ϊ����ȡ��PDF�ļ��� 
    for item in wordItems:       #����ÿ���ַ��� 
      if re.match('.*\.csv.gz$', item):   #����CSV���ļ��� 
        PDFName = item     #���ҵ�PDF�ļ��� 
    localPDF = localDir + PDFName      #�����ش洢Ŀ¼����Ҫ��ȡ��PDF�ļ����������� 
    try:            
      urllib.urlretrieve(everyURL, localPDF) #����url�������أ��������ļ����洢������Ŀ¼ 
    except Exception,e: 
      continue
  
getPDFFromNet('http://api.bitcoincharts.com/v1/csv/')
print "finish"
