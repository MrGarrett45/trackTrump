#! python3
#Track trump stats. Works with the shelve module containing all the data and writes it into a text file for easy viewing. 

#FOR STATS: use list(trumpData.values())[0].get('percent') to get a specific percent. Or just trumpData['key'].get('percent'). Also len(trumpData) to get length

import shelve, os, datetime

trumpData = shelve.open('trumpData')

totalNum = 0
for i in range(len(trumpData)):
    print(list(trumpData.values())[i].get('numArticles'))
    totalNum += list(trumpData.values())[i].get('numArticles')

avg = totalNum/len(trumpData)
avgP = avg/27

print("The percent of Trump based articles so far is %f" % avgP)
print("The average number of articles thus far is %f per 27" % avg)

now = datetime.datetime.now()
month = str(now.month)  
day = str(now.day)                             
key = month+day

todayNum = list(trumpData.values())[len(trumpData)-1].get('numArticles')
todayAvg = list(trumpData.values())[len(trumpData)-1].get('percent')
largestFlag = True
smallestFlag = True

for j in range(len(trumpData) -1):
    articleNum = list(trumpData.values())[j].get('numArticles')
    
    if todayNum < articleNum:
        largestFlag = False

    if todayNum > articleNum:
        smallestFlag = False

resultFile = open('RESULTS.txt', 'a')
resultFile.write('\nData for %s/%s/%s:\n' % (month, day, str(now.year))) 
resultFile.write('Today %f percent of articles were based on Trump,' % (todayAvg*100))
resultFile.write(' or %d out of 27\n' % todayNum)
if largestFlag == True:
    resultFile.write("Thats a new high!\n")
if smallestFlag == True:
    resultFile.write("That's a new low!\n")
resultFile.write('Since this experiment started %f percent of articles on the frontpage of r/politics have been based on Trump, or %f per 27\n' % (avgP*100, avg))

trumpData.close()
resultFile.close()

