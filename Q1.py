# -*- coding: utf-8 -*-
"""
Created on Tue May  2 22:42:34 2023

@author: Abhi9
"""

def palin(str):
    c=0
    for i in range(len(str)):
        substr=''
        
        for j in range(i+1,len(str)+1):
            substr=str[i:j]
            
            if (substr==substr[::-1]):
                print(substr,'is palindrom')
                c+=1
                
            else:
                print(substr,'is not palindrom')
    print(c)
print(palin('ghghg'))
              