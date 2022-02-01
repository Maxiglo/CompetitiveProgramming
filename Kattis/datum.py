d,m=map(int,input().split())

import datetime
import calendar
 
def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])
date = str(d)+' '+str(m)+' '+'2009'
print(findDay(date))