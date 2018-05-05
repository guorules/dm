Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> import re
>>> import numpy as np
>>> a=[]
>>> b=[]
>>> os.chdir("C://Users//wangshaoxin//Desktop//datawajue//4.27")
>>> txt = open("text1.txt", "r").read()
>>> a.append(len(re.findall("Messi", txt)))
>>> a.append(len(re.findall("Barcelona", txt)))
>>> a.append(len(re.findall("Suarez", txt)))
>>> a.append(len(re.findall("Title", txt)))
>>> a.append(len(re.findall("Soccer", txt)))
>>> txt = open("text2.txt", "r").read()
>>> b.append(len(re.findall("Messi", txt)))
>>> b.append(len(re.findall("Barcelona", txt)))
>>> b.append(len(re.findall("Suarez", txt)))
>>> b.append(len(re.findall("Title", txt)))
>>> b.append(len(re.findall("Soccer", txt)))

>>> def Cosine(vec1, vec2):
    npvec1, npvec2 = np.array(vec1), np.array(vec2)
    return npvec1.dot(npvec2)/(math.sqrt((npvec1**2).sum()) * math.sqrt((npvec2**2).sum()))

>>> Cosine(a,b)


