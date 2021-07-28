import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

def wordcloudcreation(file):
    with open(file+".txt", encoding='utf-8') as f:
        text = f.read()
        print(text)
        stopwords = set(STOPWORDS)
        stopwords.add("will")
        stopwords.add("use")
        stopwords.add("need")
        stopwords.add("see")
        stopwords.add("https")
        stopwords.add("know")
        stopwords.add("one")
        stopwords.add("using")
        stopwords.add("Thank")
        stopwords.add("work")
        stopwords.add("new")
        stopwords.add("may")
        stopwords.add("n")
        stopwords.add("go")
        stopwords.add("used")
        stopwords.add("o")
        stopwords.add("want")
        stopwords.add("thing")
        stopwords.add("try")
        stopwords.add("look")
        stopwords.add("way")
        stopwords.add("I")
        stopwords.add("Thanks")
        stopwords.add("now")
        stopwords.add("still")
        stopwords.add("good")
        stopwords.add("even")

        wc = WordCloud(max_words=3000, stopwords=stopwords, margin=10,
                    random_state=1).generate(text)
        
        default_colors = wc.to_array()
        plt.title(file)
        plt.imshow(default_colors, interpolation="bilinear")
        plt.axis("off")
        plt.show()


def frequentlyusedwords(file):
    
    output=open(file+"-toplist.txt", "w+", encoding="UTF-8")

    with open(file+".txt", encoding='utf-8') as f:
        text = f.read()
        words = {}
        
        for word in text.split():
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1
              
    toplist = [(v, k) for k, v in words.items()]
    toplist.sort()
    toplist.reverse()

    for count, word in toplist[:300]:
        print(count, word)
        output.write(str(count)+"\t"+str(word)+"\n")


    x = [toplist[:100][i][1] for i in range(0,100)]
    y = [toplist[:100][i][0] for i in range(0,100)]

    plt.figure(figsize=(20,8))
    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.xlim(-1,100)
    plt.show()
