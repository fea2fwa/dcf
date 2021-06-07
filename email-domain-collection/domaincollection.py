with open('emaillist.txt', encoding='utf-8') as rf:
    with open('domain-list.txt', 'w', encoding='utf-8') as wf:
        for row in rf:
            columns = row.rstrip().split('@')
            emaildomain = columns[1]
            wf.write(emaildomain+'\n')
