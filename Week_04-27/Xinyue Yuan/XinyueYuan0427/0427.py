#coding=utf-8
import os
import re
from collections import Counter
Keywords=["MESSI","BARCELONA","SUAREZ","TITLE","SOCCER"]
sumsdata1=[]
sumsdata2=[]
d1=[]
d2=[]
f=open("document1.txt")
lines=f.readlines()
for line in lines:
    line.strip('\n')#delete the last space
    data=re.findall(r"\w+",line)
    for x in data:
        if len(x):
            sumsdata1+=[x.upper()]
cnt1=Counter()
for word in sumsdata1:
    cnt1[word]+=1
cnt1=dict(cnt1)
for key in Keywords:
    if key in cnt1:
        d1.append(cnt1[key])
    else:
        d1.append(0)
f.close()
f=open("document2.txt")
lines=f.readlines()
for line in lines:
    line.strip('\n')#delete the last space
    data=re.findall(r"\w+",line)
    for x in data:
        if len(x):
            sumsdata2+=[x.upper()]
cnt2=Counter()
for word in sumsdata2:
    cnt2[word]+=1
cnt2=dict(cnt2)
for key in Keywords:
    if key in cnt2:
        d2.append(cnt2[key])
    else:
        d2.append(0)
f.close()

x=y=0
sum1=0
sum2=0
for i in range(0,5):
    x+=d1[i]*d2[i]
for i in range(0,5):
    sum1+=d1[i]*d1[i]
    sum2+=d2[i]*d2[i]
y=(sum1**0.5)*(sum2**0.5)

fw=open('output.txt','w')
fw.write("Frequency of Document1 Keywords:\n")
for i in range(0,5):
    fw.write(Keywords[i]+": "+str(d1[i])+"\n")
fw.write("Frequency of Document2 Keywords:\n")
for i in range(0,5):
    fw.write(Keywords[i]+": "+str(d2[i])+"\n")
fw.write("\n")
fw.write ("Cosine Similarity: ")
fw.write (str(x/y))
fw.close()

