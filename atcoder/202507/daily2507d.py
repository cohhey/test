# 文字列の「na」を「nya」に置き換える問題
# 文字列S中の連続する「na」をすべて「nya」に置き換える

# 入力を受け取る
N = int(input())
S = input()

# 「na」を「nya」に置き換える
result = S.replace("na", "nya")

print(result)