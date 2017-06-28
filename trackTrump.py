#! python3
#Track trump: compiling the percentage of articles on r/politics that are about trump. Will probably try to do over a sample period of around 20 days and publish results

import requests, sys, bs4, shelve, datetime, time
import tTrumpStats, trumpTrackerBot

def getSite():
    while True:
        url = 'https://www.reddit.com/r/politics/'             
        res = requests.get(url)             #Getting the HTML for the page
        try:
            res.raise_for_status()
        except:
            pass
            print("Failed")
        else:
            break
        time.sleep(2)        
    return res.text

theText = getSite()
soup = bs4.BeautifulSoup(theText, "html.parser")
pic = soup.select('.title')                    #Finding titles with bs
#print(len(pic))

del pic[0]
titleList = pic[1::2] 

for j in range(len(titleList)-1):              #Identifies stickied posts and deletes them               
    if titleList[j].getText().find("self") != -1:
        del titleList[j]
        continue

del titleList[(len(titleList)-1)]
                                               #After these deletions titleList now contains the 25 corrent frontpage titles
trumpCounter = 0
russiaCounter = 0
tNrCounter = 0
for i in range(len(titleList)-1):
    print(titleList[i].getText())
    titleText = titleList[i].getText()
    #print(i)

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

now = datetime.datetime.now()
month = str(now.month)                         #Will use the date as the key for
day = str(now.day)                             #the shelf file
key = month+day             

trumpData = shelve.open('trumpData')
trumpData[key] = {'percent': dailyPercent, 'numArticles': trumpCounter}
print(list(trumpData.values()))
trumpData.close()

tTrumpStats.run()         #calls the function to make the stats
time.sleep(1)             #sleep so the RESULTS.txt file has time to populate
trumpTrackerBot.runBot()  #calle the function to run the reddit bot
sys.exit()
