# E - Path Graph
# パスグラフの条件
# 辺数: N頂点のパスグラフは正確にN-1本の辺を持つ
# 次数分布:
# 次数1の頂点が正確に2個（両端点）
# 次数2の頂点がN-2個（中間点）
# 次数3以上の頂点は存在しない
# 連結性: グラフが連結している
# アルゴリズムの流れ
# 辺数チェック: M ≠ N-1なら即座に"No"
# 隣接リスト構築: グラフの構造を表現
# 次数計算: 各頂点の次数を計算
# 次数分布確認: パスグラフの次数分布と一致するかチェック
# 連結性確認: BFSでグラフが連結かチェック

from collections import defaultdict, deque

def is_connected(adj_list, n):
    """グラフが連結かどうかをBFSで確認"""
    if not adj_list:  # 辺が存在しない場合
        return n == 1  # 頂点が1つだけなら連結
    
    # 最初の頂点から開始
    start = next(iter(adj_list.keys()))
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        v = queue.popleft()
        for neighbor in adj_list[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # すべての頂点が訪問されたかチェック
    return len(visited) == n

def solve():
    N, M = map(int, input().split())
    
    # パスグラフの必要条件：辺数がN-1個
    if M != N - 1:
        # 残りの入力を読み捨て
        for _ in range(M):
            input()
        return "No"
    
    # 隣接リストを作成
    adj_list = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # 各頂点の次数をカウント
    degree = [0] * (N + 1)
    for v in range(1, N + 1):
        degree[v] = len(adj_list[v])
    
    # 次数の分布をチェック
    degree_1_count = 0  # 次数1の頂点数（両端）
    degree_2_count = 0  # 次数2の頂点数（中間点）
    
    for v in range(1, N + 1):
        if degree[v] == 1:
            degree_1_count += 1
        elif degree[v] == 2:
            degree_2_count += 1
        elif degree[v] > 2:
            return "No"  # 次数3以上の頂点があるとパスグラフではない
    
    # パスグラフの条件：
    # - 次数1の頂点が正確に2個（両端）
    # - 次数2の頂点がN-2個（中間点）
    # - 連結グラフである
    if degree_1_count == 2 and degree_2_count == N - 2 and is_connected(adj_list, N):
        return "Yes"
    else:
        return "No"

print(solve())