# trackTrump
Started this project because I started feeling like every single news article I've been reading is about Trump and want to get an exact percent.

Uses webscraping with python to track how many articles are about Trump on the frontpage of r/politics at any given time, as well as average the data out over a given time period, and then posts the results both in RESULTS.txt and r/trumpPercent.

trackTrump.py is responsible for gathering the data from reddit, parsing it, and storing the daily data in the shelve module

tTrumpStats.py is responsible for interpreting this data and providing output to the RESULTS.txt

trumpTrackerBot.py then takes the data created by tTrumpStats.py and posts it on r/trumpPercent

The program is run by simply running trackTrump.py once per day, I try to do it at 2pm everyday for consistency. Might get a raspberry pi and put this on it so it runs 24/7, but for now don't want to leave it up on my computer.

Check out RESULTS.txt or r/trumpPercent for updated information!

Update 6/28: Found workarounds for reddit saying too many requests, also working on putting the program on raspberry pi and automating with a cron job. 
