# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 00:52:54 2021

@author: David_Chu
"""
import scapy.all as scapy

def sniff(filter_IP):
    scapy.sniff(filter = "ip src " + str(filter_IP), prn=lambda x:x.summary())

def sniff():
    scapy.sniff(prn=lambda x:x.summary())

filter_IP = str(input("請輸入篩選IP : "))    


if filter_IP:
    sniff(filter_IP)


if filter_IP == "":
    sniff()



    
