# E - Loong Tracking の解答

from collections import deque

def solve():
    N, Q = map(int, input().split())
    
    # 龍の各パーツの初期位置
    # パーツ i は座標 (i, 0) にある
    dragon = [(i, 0) for i in range(1, N + 1)]
    
    # 方向の定義
    directions = {
        'R': (1, 0),   # x軸正方向
        'L': (-1, 0),  # x軸負方向
        'U': (0, 1),   # y軸正方向
        'D': (0, -1)   # y軸負方向
    }
    
    for _ in range(Q):
        query = input().split()
        
        if query[0] == '1':
            # 頭を移動
            direction = query[1]
            dx, dy = directions[direction]
            
            # 現在の頭の位置
            head_x, head_y = dragon[0]
            
            # 新しい頭の位置
            new_head_x = head_x + dx
            new_head_y = head_y + dy
            
            # 各パーツを更新（後ろから前へ）
            for i in range(N - 1, 0, -1):
                dragon[i] = dragon[i - 1]
            
            # 頭を新しい位置に移動
            dragon[0] = (new_head_x, new_head_y)
            
        elif query[0] == '2':
            # パーツの位置を出力
            p = int(query[1])
            x, y = dragon[p - 1]  # 1-indexedなので-1
            print(x, y)

solve()