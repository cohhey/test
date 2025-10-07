# H - Train Delay の解答

from collections import defaultdict

def solve():
    N, M, X1 = map(int, input().split())
    
    trains = []
    for i in range(M):
        a, b, s, t = map(int, input().split())
        trains.append((a, b, s, t))
    
    # X[0] = X1 (1-indexed を 0-indexed に変換)
    X = [0] * M
    X[0] = X1
    
    # 乗り換え可能な電車の組を見つけて制約を作成
    constraints = []
    for i in range(M):
        for j in range(M):
            if i != j:
                a_i, b_i, s_i, t_i = trains[i]
                a_j, b_j, s_j, t_j = trains[j]
                
                # B_i = A_j かつ T_i ≤ S_j なら乗り換え可能
                if b_i == a_j and t_i <= s_j:
                    # 制約: T_i + X_i ≤ S_j + X_j
                    # つまり X_j ≥ T_i + X_i - S_j
                    constraints.append((i, j, t_i - s_j))
    
    # 反復的に制約を満たすまでX値を更新
    changed = True
    while changed:
        changed = False
        for i, j, diff in constraints:
            # X_j ≥ X_i + diff
            required = X[i] + diff
            if required > X[j]:
                X[j] = required
                changed = True
    
    # 結果を出力（X2からXM、つまりX[1]からX[M-1]）
    result = X[1:]
    print(*result)

solve()