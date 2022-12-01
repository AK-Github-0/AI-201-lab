# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:41:00 2021

@author: AK(2020024)
"""

def encryption(string,shift):
    Encrypted = ""
    for i in range(len(string)):
        char = string[i]
        Encrypted += chr((ord(char) + shift-65) % 26 + 65)
 
    return Encrypted

print(encryption("AK",1))
