import datetime

with open('easyinput.txt', 'r') as f:
    dates = [date.split() for date in f.readlines()]
    dateobjects = [datetime.date(int(date[0]), int(date[1]), int(date[2])) for date in dates]

today = datetime.date.today()
for dateobject in dateobjects:
    print "%d more days until %s" % ((dateobject - today).days,
            dateobject.isoformat())

