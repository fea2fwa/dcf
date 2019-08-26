from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#from datetime import datetime
import datetime

csvoutput=open("dcfJapanese.csv", "w+", encoding="UTF-8")
output=open("dcfJapanese.txt", "w+", encoding="UTF-8")

def joinedusers(bsObj):
        questioners = []
        for questioner in bsObj.find_all("a", {"class":"lia-link-navigation lia-page-link lia-user-name-link"}):
            questioners += questioner

        usernames = {}        
        for questioner in questioners:
            questioner = questioner.get_text()
            if questioner not in usernames.values():
                new_id = len(usernames)
                usernames[new_id] = questioner
        print(usernames)
        
        return usernames


with open('url.txt', encoding='utf-8') as f:
    for row in f:
        url = row.rstrip()
        html = urlopen(url)
        bsObj = BeautifulSoup(html)
        bodytext = bsObj.findAll("div", {"class":"lia-message-body-content"})
        bodydate = bsObj.findAll("span", {"class":"local-date"})
        bodytime = bsObj.findAll("span", {"class":"local-time"})
        title = bsObj.title.get_text()
        title = title.strip(" - Dell Community")
        if "解決済み:" in title:
            title = title.strip("解決済み: ")

        usernames = joinedusers(bsObj)
        questioner = usernames[0]
        replyer = []

        for i in range(1, len(usernames)):
            print(usernames[i])
            replyer += usernames[i]
        
        print(replyer)

        for body in bodytext:
            print(body.get_text()+"\n")
            output.write(body.get_text()+"\n")
        dummy = 0
        for ddata, tdata in zip (bodydate, bodytime):
            dtsource = ddata.get_text()+" "+tdata.get_text()
            x = datetime.datetime.strptime(dtsource.strip('\u200e'), '%m-%d-%Y %I:%M %p')+datetime.timedelta(hours=16)
            if dummy == 0:
                dtime1 = x.strftime('%Y/%m/%d %H:%M')
            elif dummy == 1:
                dtime2 = x.strftime('%Y/%m/%d %H:%M')
                csvoutput.write(url+","+title+","+questioner+","+dtime1+","+dtime2)
                for i in range(1, len(usernames)):
                    csvoutput.write(","+usernames[i])
                csvoutput.write("\n")
            else: 
                break
            dummy += 1

        if dummy == 1:
             csvoutput.write(url+","+title+","+questioner+","+dtime1+",""\n")
            
            
            


csvoutput.close()
output.close()


