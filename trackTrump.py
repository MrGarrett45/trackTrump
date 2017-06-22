#! python3
#Track trump: compiling the percentage of articles on r/politics that are about trump. Will probably try to do over a sample period of around 20 days and publish results

import requests, os, bs4, shelve

url = 'https://www.reddit.com/r/politics/'             
#os.makedirs('C:\\Users\\gmclaughlin\\Python\\trumpPercent')  

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
pic = soup.select('.title')
#print(len(pic))

del pic[0]
del pic[0]
del pic[55:57]

titleList = pic[1::2]
trumpCounter = 0
for i in range(len(titleList)-1):
    print(titleList[i].getText())
    #titleText = titleList[i].getText()
    
    if titleText.find("Trump") != -1:
        trumpCounter = trumpCounter + 1
        #print(trumpCounter)

dailyPercent = trumpCounter/len(titleList)
print("Todays trump percent is: %f" % dailyPercent)
