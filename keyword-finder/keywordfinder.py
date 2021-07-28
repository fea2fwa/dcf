from stats import wordcloudcreation,frequentlyusedwords

filenames = ["storage_urls-texts","poweredge_urls-texts","networking_urls-texts","total-texts"]

for file in filenames:
    wordcloudcreation(file)
    frequentlyusedwords(file)