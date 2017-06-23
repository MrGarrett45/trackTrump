# trackTrump
Started this project because I started feeling like every single news article I've been reading is about Trump and want to get an exact percent.

Uses webscraping with python to track how many articles are about Trump on the frontpage of r/politics at any given time, as well as average the data out over a given time period.

trackTrump.py is responsible for gathering the data from reddit, parsing it, and storing the daily data in the shelve module

tTrumpStats.py is responsible for interpreting this data and providing output to the RESULTS.txt

Each of those .py files need to be updated once a day (going to try to update at around 2pm everyday for consistency), looking into a way to automate it but don't really want to leave it running all the time.

Might make a reddit bot to post the info to a subreddit and also might make some kind of graph to display the data over time.

Only issue is that reddit will flag trackTrump.py for too many requests but if you just submit it a few times it will go through.

Check out RESULTS.txt for updated information!
