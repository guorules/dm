Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> import re
>>> import numpy as np
>>> import math
>>> a=[]
>>> b=[]
>>> os.chdir("C://Users//wangshaoxin//Desktop//datawajue//4.27")
>>> txt = open("text1.txt", "r").read().lower()
>>> a.append(len(re.findall("messi", txt)))
>>> a.append(len(re.findall("barcelona", txt)))
>>> a.append(len(re.findall("suarez", txt)))
>>> a.append(len(re.findall("title", txt)))
>>> a.append(len(re.findall("soccer", txt)))
>>> txt = open("text2.txt", "r").read().lower()
>>> b.append(len(re.findall("messi", txt)))
>>> b.append(len(re.findall("barcelona", txt)))
>>> b.append(len(re.findall("suarez", txt)))
>>> b.append(len(re.findall("title", txt)))
>>> b.append(len(re.findall("soccer", txt)))

>>> def Cosine(vec1, vec2):
    npvec1, npvec2 = np.array(vec1), np.array(vec2)
    return npvec1.dot(npvec2)/(math.sqrt((npvec1**2).sum()) * math.sqrt((npvec2**2).sum()))

>>> Cosine(a,b)


