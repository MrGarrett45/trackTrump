#! python3
#Reddit bot to post to r/trumpToday

from selenium import webdriver 
import datetime, os

resultFile = open('RESULTS.txt', 'r')

i = 0
for i in resultFile:
    i = i + 1
print(i)
