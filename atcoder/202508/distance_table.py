# D - Distance Table
# N個の駅が直線上に並んでいて、隣接駅間の距離が与えられる
# 各駅ペア間の距離を指定された形式で出力する

# 入力を受け取る
N = int(input())
D = list(map(int, input().split()))

# 各行を出力
for i in range(1, N):  # i行目（1からN-1行）
    distances = []
    
    # i行目のj番目は駅iと駅(i+j)の間の距離
    for j in range(1, N - i + 1):  # j番目（1からN-i個）
        # 駅iと駅(i+j)の間の距離を計算
        # これは D[i-1] + D[i] + ... + D[i+j-2] の和
        distance = 0
        for k in range(i - 1, i + j - 1):  # D[i-1]からD[i+j-2]まで
            distance += D[k]
        distances.append(distance)
    
    # 空白区切りで出力
    print(' '.join(map(str, distances)))