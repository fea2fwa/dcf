
with open('existing_email_list.txt', encoding='utf-8') as fe:
    existing_emails=[]
    for row in fe:
        existing_email = row.lower().rstrip()
        existing_emails.append(existing_email)

    print(existing_emails)


with open('new_user_list.txt', encoding='utf-8') as fn:
    new_users={}
    for row in fn:
        new_user = row.rstrip().split('	')
        user_id = new_user[0]
        user_email = new_user[1].lower()
        new_users[user_id] = user_email

    print(new_users)


with open('usename_change_needed.txt', 'w', encoding='utf-8') as fc:
    with open('add_user_needed.txt', 'w', encoding='utf-8') as fa:
        for k,v in new_users.items():
            if v in existing_emails:
                fc.write(k+','+v+'\n')
            if v not in existing_emails:
                fa.write(k+','+v+'\n')

