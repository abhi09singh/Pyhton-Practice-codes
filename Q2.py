# -*- coding: utf-8 -*-
"""
Created on Wed May  3 20:13:50 2023

@author: Abhi9


Following is format of a log message from server
"<msg><space><ip address>"
Ex. "Too busy 10.0.0.1"
"Invalid Request 12.138.45.45"
Seperate every word from the message
If there is special character in message then
print ("Error in message")
Store ip address seperately. Check if ip address is valid
if not valid then print("Error") if valid then print("valid log message ")

case 1 3 marks "Too busy 10.0.0.1" o/p "valid log message"

case 2 3 marks "Invalid Request 12.138.45.45" 
o/p "valid log message"
case 3 4 marks "Extreme Load A.B.10.90" o/p "Error"

case4 10 marks Program should work for any unknown input

"""
msg=input("<msg><space><ip address> :")

def chk(msg):
    smsg=msg.split()
    ip=smsg[2]
    sip=ip.split('.')
    for idx in sip:
        if (idx.isnumeric()==True):
            return chk1(msg)
        elif(idx.isnumeric()==False):
            return ('Error')
        
def chk1(msg):
    smsg=msg.split()
    cmsg=smsg[:-1]
    for idx in cmsg:
        if (idx.isalpha()):
            return 'valid log message'
        else:
            return 'error'

print(chk(msg))
