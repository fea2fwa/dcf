with open("new.txt", encoding='UTF-8') as repf:
    repliers = {}
    for row in repf:
        users = []
        users = row.rstrip().split('\t')
        #print(users)
        for user in users:
            if user in repliers.keys():
                if user != '':
                    repliers[user] += 1
            else:
                if user != '':
                    repliers[user] = 1
                    
print(repliers)

with open("userstats.txt", "w+", encoding="UTF-8") as wf:
    for k,v in repliers.items():
        wf.write(k+"\t"+str(v)+"\n")

