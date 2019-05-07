with open('contentPVranking.txt', encoding='utf-8') as rf:
	with open('redirecturls.txt', 'w', encoding='utf-8') as wf:
		for row in rf:
                    columns = row.rstrip().split(',')
                    docid = columns[0]
                    title = columns[1]
                    pagev = columns[2]
                    if len(docid) > 5:
                        continue
                    else:
                        wf.write(str(title)+','+'https://community.emc.com/docs/DOC-'+str(docid)+','+str(pagev)+'\n')


