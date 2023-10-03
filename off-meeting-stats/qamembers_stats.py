filename= input("Input file name? : ")

def member_count(dicdata):
    for k, v in sorted(dicdata.items(), key=lambda x: -x[1]):
        print(k+';'+str(v))

    print('\n')

nameNo = {}


with open(filename, encoding='utf-8') as f:
    for row in f:
        name = row.rstrip()
        
        if name in nameNo.keys():
            nameNo[name] += 1
        else:
            nameNo[name] = 1
        
member_count(nameNo)
