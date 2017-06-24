#! python3
#Track trump: compiling the percentage of articles on r/politics that are about trump. Will probably try to do over a sample period of around 20 days and publish results

import requests, os, bs4, shelve, datetime

url = 'https://www.reddit.com/r/politics/'             
res = requests.get(url)                        #Getting the HTML for the page
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
pic = soup.select('.title')                    #Finding titles with bs
#print(len(pic))

now = datetime.datetime.now()
month = str(now.month)                         #Will use the date as the key for
day = str(now.day)                             #the shelf file
key = month+day             

del pic[0]
del pic[0]
del pic[0]
del pic[0]
del pic[0]
del pic[53:55]
titleList = pic[1::2]

trumpCounter = 0
russiaCounter = 0
tNrCounter = 0
for i in range(len(titleList)-1):
    print(titleList[i].getText())
    titleText = titleList[i].getText()
    
    if titleText.find("Trump") != -1:
        trumpCounter = trumpCounter + 1
        #print(trumpCounter)

    if titleText.find("Russia") != -1  or titleText.find("Putin") != -1 or titleText.find("Kremlin") != -1:
	russiaCounter = russiaCounter + 1

    if titleText.find("Trump") != -1 and (titleText.find("Russia") != -1  or titleText.find("Putin") != -1 or titleText.find("Kremlin") != -1):
	tNrCounter = tNrCounter + 1

dailyPercent = trumpCounter/(len(titleList)-1)
print("Today %d out of %d articles were about Trump" % (trumpCounter, (len(titleList)-1)))
print("Todays trump percent is: %f" % dailyPercent)

trumpData = shelve.open('trumpData')
trumpData[key] = {'percent': dailyPercent, 'numArticles': trumpCounter}
print(list(trumpData.values()))
trumpData.close()
