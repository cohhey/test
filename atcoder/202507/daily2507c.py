# 配列から末尾要素を削除して1からMまでの数がすべて含まれないようにする問題
# 必要な操作回数の最小値を求める

# 入力を受け取る
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 操作回数をカウント
operations = 0

# 1からMまでのすべての数が含まれている間は削除を続ける
while len(A) > 0:
    # 現在の配列に1からMまでのすべての数が含まれているかチェック
    A_set = set(A)
    all_contained = True
    
    for i in range(1, M + 1):
        if i not in A_set:
            all_contained = False
            break
    
    # 1からMまでのすべての数が含まれていない場合は操作終了
    if not all_contained:
        break
    
    # 末尾の要素を削除
    A.pop()
    operations += 1

print(operations)