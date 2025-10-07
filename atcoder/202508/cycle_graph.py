# E - Cycle Graph?
# N頂点M辺の単純無向グラフがサイクルグラフかどうかを判定

def is_cycle_graph(N, M, edges):
    # サイクルグラフの必要条件：辺数がN個
    if M != N:
        return False
    
    # 各頂点の次数をカウント
    degree = [0] * (N + 1)
    
    # 隣接リストを作成（連結性チェック用）
    adj = [[] for _ in range(N + 1)]
    
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
        adj[a].append(b)
        adj[b].append(a)
    
    # すべての頂点の次数が2でなければサイクルグラフではない
    for i in range(1, N + 1):
        if degree[i] != 2:
            return False
    
    # 連結性をチェック（DFSで全頂点に到達できるか）
    visited = [False] * (N + 1)
    
    def dfs(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                dfs(u)
    
    # 頂点1から開始
    dfs(1)
    
    # すべての頂点が訪問されたかチェック
    for i in range(1, N + 1):
        if not visited[i]:
            return False
    
    return True

# 入力を受け取る
N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))

# サイクルグラフかどうか判定
if is_cycle_graph(N, M, edges):
    print("Yes")
else:
    print("No")