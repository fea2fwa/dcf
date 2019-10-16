import re
import collections
from html import unescape
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

startId=input("Enter the first thread#: ")
endId=input("Enter the last thread#: ")

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
        
        return usernames

with open("dcfstats.txt", "w+", encoding="UTF-8") as textoutput:

    for i in range(int(startId), int(endId)+1):
        try:
            url = "https://www.dell.com/community/forums/v4/forumtopicpage/message-uid/"+str(i)
            html=urlopen(url)
        except:
            print("Thread#"+str(i)+" has been deleted or is an invalid or private thread.")
        else:
            bsObj = BeautifulSoup(html)
            bodydate = bsObj.findAll("span", {"class":"local-date"})
            bodytime = bsObj.findAll("span", {"class":"local-time"})
            space_id_obj = bsObj.find_all("link", class_="lia-link-navigation hidden live-links")
            title = bsObj.title.get_text()
            title = title.strip(" - Dell Community")

            space_id_obj = str(space_id_obj)
            spacename = re.findall(r"board.id=.*&amp;",space_id_obj)
            spacename = str(spacename)
            splittext = spacename.split('&')
            spacename = splittext[0]
            spacename = spacename[11:]

            markanswered = "not-marked"
            if "解決済み:" in title:
                title = title.strip("解決済み: ")
                markanswered = "markanswered"

            if "Solved:" in title:
                title = title.strip("Solved: ")
                markanswered = "markanswered"

            if "Re:" in title:
                title = title.strip("Re: ")

            if "RE:" in title:
                title = title.strip("RE: ")

            if "回复：" in title:
                title = title.strip("回复： ")


            usernames = joinedusers(bsObj)
            
            try:
               questioner = usernames[0]
            except:
               questioner = "n/a(spam?)"

            replyer = []

            for i in range(1, len(usernames)):
                replyer += usernames[i]

            dummy = 0
            for ddata, tdata in zip (bodydate, bodytime):
                dtsource = ddata.get_text()+" "+tdata.get_text()
                x = datetime.datetime.strptime(dtsource.strip('\u200e'), '%m-%d-%Y %I:%M %p')+datetime.timedelta(hours=16)
                if dummy == 0:
                    dtime1 = x.strftime('%Y/%m/%d %H:%M')
                elif dummy == 1:
                    dtime2 = x.strftime('%Y/%m/%d %H:%M')
                    textoutput.write(url+"\t"+spacename+"\t"+title+"\t"+questioner+"\t"+dtime1+"\t"+dtime2+"\t"+markanswered)
                    for i in range(1, len(usernames)):
                        textoutput.write("\t"+usernames[i])
                    textoutput.write("\n")
                else: 
                    break
                dummy += 1

            if dummy == 1:
                textoutput.write(url+"\t"+spacename+"\t"+title+"\t"+questioner+"\t"+dtime1+"\t"+"\t"+"\t"+"\n")

