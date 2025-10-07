# G - Snuke Maze の解答

from collections import deque

def solve():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(input().strip())
    
    # "snuke"のパターン
    pattern = "snuke"
    
    # BFSで探索
    # 状態: (行, 列, パターンでの位置)
    queue = deque()
    visited = set()
    
    # 開始点が's'かチェック
    if grid[0][0] == 's':
        queue.append((0, 0, 0))  # (行, 列, snukeでの位置)
        visited.add((0, 0, 0))
    
    # 4方向への移動
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        row, col, pattern_pos = queue.popleft()
        
        # ゴールに到達したかチェック
        if row == H - 1 and col == W - 1:
            return "Yes"
        
        # 次の文字の位置を計算
        next_pattern_pos = (pattern_pos + 1) % 5
        next_char = pattern[next_pattern_pos]
        
        # 4方向に移動を試す
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            
            # 範囲チェック
            if 0 <= new_row < H and 0 <= new_col < W:
                # 次の文字が期待する文字と一致するかチェック
                if grid[new_row][new_col] == next_char:
                    new_state = (new_row, new_col, next_pattern_pos)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
    
    return "No"

print(solve())