# -*- coding: utf-8 -*-
"""buffon's needle problem

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KY8yDg3msxl5bodlfJ66jFcWbg1xAdcZ
"""

import random
import math
n=10000
#length of needle
l=4
#width between parallel lines
d=25
#size of paper
p=100
count=0

for i in range(n):
  theta=random.uniform(0,2*math.pi)
  y1=random.uniform(0,p)
  y2=y1+l*math.sin(theta)
  miny=math.ceil(min(y1,y2))
  maxy=math.floor(max(y1,y2))
  flag=0
  for i in range(miny,maxy+1):
    if i%d==0:
      flag=1
  if flag==1:
    count+=1

prob=count/n
print("pi value ",(2*l)/(prob*d))

