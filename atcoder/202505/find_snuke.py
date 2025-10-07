# C - Find snuke

# グリッドの読み込み: H×Wのマス目を文字列配列として格納
# 8方向の探索: 各マスから8方向（上下左右と4つの斜め）に向かって"snuke"を探索
# 範囲チェック: 5文字分の範囲がマス目内に収まるかチェック
# 文字列マッチング: 指定方向に"snuke"が並んでいるかチェック
# 座標出力: 見つかった5つのマスの座標を1-indexedで出力

# 入力を読み込む
H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(input().strip())

# 8方向のベクトル (行の変化量, 列の変化量)
directions = [
    (-1, -1), (-1, 0), (-1, 1),  # 左上、上、右上
    (0, -1),           (0, 1),   # 左、右
    (1, -1),  (1, 0),  (1, 1)    # 左下、下、右下
]

target = "snuke"

def is_valid(r, c):
    """座標が範囲内かチェック"""
    return 0 <= r < H and 0 <= c < W

def find_snuke():
    """snukeが並んでいる場所を探す"""
    for r in range(H):
        for c in range(W):
            # 各方向を試す
            for dr, dc in directions:
                # この方向で5文字すべてが範囲内かチェック
                valid = True
                for i in range(5):
                    nr, nc = r + i * dr, c + i * dc
                    if not is_valid(nr, nc):
                        valid = False
                        break
                
                if not valid:
                    continue
                
                # この方向で"snuke"が並んでいるかチェック
                found = True
                for i in range(5):
                    nr, nc = r + i * dr, c + i * dc
                    if grid[nr][nc] != target[i]:
                        found = False
                        break
                
                if found:
                    # 見つかった場合、座標を返す
                    result = []
                    for i in range(5):
                        nr, nc = r + i * dr, c + i * dc
                        result.append((nr + 1, nc + 1))  # 1-indexedに変換
                    return result
    
    return None

# snukeを探して結果を出力
result = find_snuke()
for r, c in result:
    print(r, c)