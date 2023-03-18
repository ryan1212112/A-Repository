# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:30:59 2022

@author: ryan
"""

score = int(input())
score = score**0.5*9+score*0.1


if score >= 90:
    print('A')
if score < 90 and score >= 80:
    print('B')
if score < 80 and score >= 70:
    print('C')
if score < 70 and score >= 60:
    print('D')
if score < 60:
    print('F')