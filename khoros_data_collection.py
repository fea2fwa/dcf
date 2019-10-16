import csv

output=open("testoutput.txt", "w+", encoding="UTF-8")

with open('lithium_api_output.csv', encoding='utf-8') as f1:
    list = []
    reader = csv.reader(f1)
    for row in reader:
            #rowinfo = row.rstrip().split(',')
            user_name = row[0]
            if not user_name == 'Anonymous':
                if 'Employee' in row[1]:
                    if user_name not in list:
                        list.append(user_name)
                        output.write(user_name+",1"+"\n")                    
                else:
                    if user_name not in list:
                        list.append(user_name)
                        output.write(user_name+",0"+"\n")



