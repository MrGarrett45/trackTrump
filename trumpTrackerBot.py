#! python3
#Reddit bot to post to r/trumpToday

from selenium import webdriver 
import datetime, os

resultFile = open('RESULTS.txt', 'r')

test = resultFile.readlines()
 print(test[len(test)-1])
