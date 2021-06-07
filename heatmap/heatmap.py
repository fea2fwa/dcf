import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from datetime import datetime as dt



def getdayinfo(file="daysdata.txt"):
       datetime_output=open("datetimedata.txt", "w+", encoding="UTF-8")
       with open(file, encoding='utf-8-sig') as f:
              for row in f:
                     tmp=row.rstrip()
                     datetimeinfo=dt.strptime(tmp, '%Y/%m/%d %H:%M').strftime('%Y/%m/%d %H:%M,%a')
                     datetime_output.write(datetimeinfo+"\n")
       
       datetime_output.close()


def mapcreation(file="datetimedata.txt"):
    hours={"00":0, "01":1, "02":2, "03":3, "04":4, "05":5,
           "06":6, "07":7, "08":8, "09":9, "10":10, "11":11,
           "12":12, "13":13, "14":14, "15":15, "16":16, "17":17,
           "18":18, "19":19, "20":20, "21":21,"22":22,"23":23}
    days={"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}
    plotdata = np.zeros([7,24])

    with open(file, encoding='utf-8') as f:
        for row in f:
           temp = row.rstrip().split(',')
           dayinfo = temp[1]
           dateinfo = temp[0].split(' ')
           hourinfo = dateinfo[1].split(':')
           hourinfo = hourinfo[0]
           
           row = int(days[dayinfo])
           column = int(hours[hourinfo])

           plotdata[[row],[column]] += 1

    
    print(plotdata)
    plt.figure()
    plt.imshow(plotdata, interpolation='nearest', cmap='jet')
    plt.colorbar()
    plt.show()