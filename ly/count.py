#! /usr/bin/env python  
#coding=utf-8  
import re   
  
def termFreq(filename):  
    text = open(filename, 'r').read()  
    wfile = open('result.txt', 'w')  
      
    words = text.split(' ')  
    dict = {}  
    for w in words:  
        if w in dict:  
            dict[w] += 1  
        else:  
            dict[w] = 1  
          
    dict = sorted(dict.items(), key = lambda d:d[1])  
      
    for a, b in dict:  
        if b > 0:  
            wfile.write(a + ' ' + str(b) + '\n')  
              
  
if __name__ == '__main__':  
    termFreq('test.txt')  
