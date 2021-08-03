# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 11:40:13 2021
HWB1 Largest formed number
@author: Mind
"""

x=[50,2,1,9]

def highestnum(l):
   for i in range(len(l)-1):
      for j in range (i+1,len(l)):
         a,b=len(str(l[i])),len(str(l[j]))
         c=min(a,b)
         if str(l[i])[:c]==str(l[j])[:c]:
            if b==max(a,b) and str(l[j])[c-1]>str(l[j])[0] :
               l[i],l[j]=l[j],l[i]
            elif a==max(a,b) and str(l[i])[c-1]<str(l[i])[0] :
               l[i],l[j]=l[j],l[i]
         for k in range (c):
            if int(str(l[i])[k])>int(str(l[j])[k]):
               break
            if int(str(l[i])[k])<int(str(l[j])[k]):
               l[i],l[j]=l[j],l[i]
               break
   return l
for i in [x]:
   print(*(highestnum(i)),sep="")