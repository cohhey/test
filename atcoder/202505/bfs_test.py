# 実際にBFSで距離を計算
from collections import deque

def bfs_jump_distance(x1, y1, x2, y2, max_steps=20):
    """BFSで実際のジャンプ距離を計算（小さい範囲のみ）"""
    if x1 == x2 and y1 == y2:
        return 0
    
    queue = deque([(x1, y1, 0)])
    visited = {(x1, y1)}
    
    # ジャンプの方向
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    while queue:
        x, y, dist = queue.popleft()
        
        if dist >= max_steps:
            break
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if nx == x2 and ny == y2:
                return dist + 1
            
            if (nx, ny) not in visited and abs(nx) <= 100 and abs(ny) <= 100:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    
    return 0  # 到達不可能

# テスト
print("BFS結果:")
print(f"(0,0) to (1,3): {bfs_jump_distance(0, 0, 1, 3)}")
print(f"(0,0) to (5,6): {bfs_jump_distance(0, 0, 5, 6)}")
print(f"(1,3) to (5,6): {bfs_jump_distance(1, 3, 5, 6)}")

# 実際の経路も確認
def find_path(x1, y1, x2, y2, max_steps=10):
    if x1 == x2 and y1 == y2:
        return [(x1, y1)]
    
    queue = deque([(x1, y1, 0, [(x1, y1)])])
    visited = {(x1, y1)}
    
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    while queue:
        x, y, dist, path = queue.popleft()
        
        if dist >= max_steps:
            break
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if nx == x2 and ny == y2:
                return path + [(nx, ny)]
            
            if (nx, ny) not in visited and abs(nx) <= 100 and abs(ny) <= 100:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1, path + [(nx, ny)]))
    
    return None

path = find_path(0, 0, 1, 3)
if path:
    print(f"経路: {path}")
    print(f"ステップ数: {len(path) - 1}")