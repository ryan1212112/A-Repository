# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 19:00:50 2022

@author: ryan
"""

Uname = input('username:')
password = input('password:')
IDnumber = input('ID number:')

PL = len(password)-2

passwordshow = password[0] + '*' * PL + password[-1]

print('username:',Uname)
print('password:',passwordshow)
print('ID numher:',IDnumber)
