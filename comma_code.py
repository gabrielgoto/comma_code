# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 10:57:20 2021

@author: PasqualeDeAngelis
"""

# From Automate2e, page 107

spam = []
spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(lst):
    counter = 0
    sentance = ''
    for i in lst:
        if counter < (len(lst) - 1):
            sentance = sentance + i + ', '
            counter += 1
        else:
            sentance = sentance + 'and ' + i 
    return sentance
        
spam = []
spam = ['apples', 'bananas', 'tofu', 'cats']
spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']

print(comma_code(spam))