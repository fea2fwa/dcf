from urllib.request import urlopen
from bs4 import BeautifulSoup


filenames = ["storage_urls","poweredge_urls","networking_urls"]


for filename in filenames:

    output=open(filename+"-texts.txt", "w+", encoding="UTF-8")

    with open(filename+".txt", encoding='utf-8') as f:
        for row in f:
            url = row.rstrip()
            html = urlopen(url)
            bsObj = BeautifulSoup(html)
            bodytext = bsObj.findAll("div", {"class":"lia-message-body-content"})
            bodydate = bsObj.findAll("span", {"class":"local-date"})
            bodytime = bsObj.findAll("span", {"class":"local-time"})
            title = bsObj.title.get_text().rstrip()
            title = title.strip("\n")
            title = title.strip("\t")
            title = title.strip("\t")
            title = title.strip(" - Dell Community")
            if "解決済み:" in title:
                title = title.strip("解決済み: ")
            if "Solved:" in title:
                title = title.strip("Solved: ")
            if "Re:" in title:
                title = title.strip("Re: ")


            for body in bodytext:
                print(title+"\n"+body.get_text()+"\n")
                output.write(title+"\n"+body.get_text()+"\n")

            
            



