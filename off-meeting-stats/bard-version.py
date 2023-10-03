import collections

# ファイルの名前を取得します。
filename = input("ファイルの名前を入力してください: ")

# ファイルを開き、文字列として読み込みます。
with open(filename, "r") as f:
  text = f.read()

# 単語をスペースで分割します。
words = text.split()

# 単語の出現回数を数えます。
counts = collections.Counter(words)

# 結果を出力します。
for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
  print(word, count)

