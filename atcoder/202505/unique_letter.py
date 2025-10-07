# B - A Unique Letter

# 長さ3の文字列Sが与えられる
# Sに1度だけ含まれる文字を1つ出力する
# そのような文字がない場合は-1を出力する

# 入力を読み込む
S = input().strip()

# 各文字の出現回数をカウント
char_count = {}
for char in S:
    char_count[char] = char_count.get(char, 0) + 1

# 1度だけ含まれる文字を探す
unique_char = None
for char in S:
    if char_count[char] == 1:
        unique_char = char
        break

# 結果を出力
if unique_char is not None:
    print(unique_char)
else:
    print(-1)