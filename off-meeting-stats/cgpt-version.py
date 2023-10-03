import re


def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()  # ファイルの内容を小文字に変換して取得

            # 正規表現を使用して単語を抽出し、出現回数をカウント
            words = re.findall(r'\b\w+\b', content)
            word_count = {}

            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            # 出現回数で降順にソート
            sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

            # 結果を表示
            for word, count in sorted_word_count:
                print(f"{word}: {count}")

    except FileNotFoundError:
        print("指定されたファイルが見つかりません。")


# ファイルパスを指定して関数を呼び出す
file_path = "./questioners.txt"
count_words(file_path)



