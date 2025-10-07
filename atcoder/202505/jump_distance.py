# H - Jump Distance Sum の解答

def jump_distance(x1, y1, x2, y2):
    """2点間のジャンプ距離を計算"""
    if x1 == x2 and y1 == y2:
        return 0
    
    # 座標の差
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # ジャンプの特性分析:
    # 各ジャンプで x座標とy座標が同時に±1変化する
    # つまり、|x|+|y| の偶奇性が保たれる
    
    if (x1 + y1) % 2 != (x2 + y2) % 2:
        return 0  # 到達不可能
    
    # チェビシェフ距離を計算
    # ジャンプの制約により、移動距離は max(dx, dy) に関連
    # ただし、斜め移動しかできないため、特殊な計算が必要
    
    # 実際の最短距離は max(dx, dy) と (dx+dy)/2 の大きい方
    diagonal_dist = max(dx, dy)
    manhattan_half = (dx + dy + 1) // 2  # 切り上げ
    
    return max(diagonal_dist, manhattan_half)

def solve():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    
    total_distance = 0
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = jump_distance(x1, y1, x2, y2)
            total_distance += distance
    
    return total_distance

print(solve())