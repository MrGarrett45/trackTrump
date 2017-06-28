#! python3
#Reddit bot to post to r/trumpPercent

from selenium import webdriver 
import datetime, os, time, sys

def runBot(): 
    resultFile = open('RESULTS.txt', 'r')

    test = resultFile.readlines()
    #print(test[len(test)-1])

    title = test[len(test)-3]
    dailyMessage = test[len(test)-2]
    statMessage = test[len(test)-1]
    textBody = dailyMessage +'\n'+ statMessage +'\n'+'visit https://github.com/rGarrett45/trackTrump to see the code and full results of this project!'
    #print(title)
    #print(dailyMessage)
    #print(statMessage)

    browser = webdriver.Firefox()
    browser.get('http://reddit.com/r/trumpPercent')

    signInElem = browser.find_element_by_link_text('Log in or sign up')
    signInElem.click()

    time.sleep(2)

    loginElem = browser.find_element_by_id('user_login')    #Logging in
    loginElem.send_keys('trumpTrackerBot')
    time.sleep(2)                                       
    passwordElem = browser.find_element_by_id('passwd_login')
    passwordElem.send_keys('passwd')
    passwordElem.submit()
    time.sleep(2)

    linkElem = browser.find_element_by_link_text('Submit a new text post')  #Sub    mitting the text post
    linkElem.click()
    time.sleep(2)
    #browser.implicitly_wait(5)
    titleElem = browser.find_element_by_name('title')
    titleElem.send_keys(title)
    time.sleep(2)
    textElem = browser.find_element_by_name('text')
    textElem.send_keys(textBody)
    time.sleep(2)
    textElem.submit()

    sys.exit()
