# I - Diversity の解答

def solve():
    N, X, K = map(int, input().split())
    items = []
    for _ in range(N):
        p, u, c = map(int, input().split())
        items.append((p, u, c))
    
    # 色ごとに商品をグループ化
    colors = {}
    for i, (p, u, c) in enumerate(items):
        if c not in colors:
            colors[c] = []
        colors[c].append((p, u))
    
    # 各色について、その色の商品だけでのナップサック問題を解く
    color_dp = {}
    for color, color_items in colors.items():
        # この色の商品だけでのDP
        dp = [-1] * (X + 1)
        dp[0] = 0
        
        for p, u in color_items:
            for w in range(X, p - 1, -1):
                if dp[w - p] != -1:
                    dp[w] = max(dp[w], dp[w - p] + u)
        
        color_dp[color] = dp
    
    color_list = list(colors.keys())
    num_colors = len(color_list)
    
    # DPで色の組み合わせを考慮
    # dp[i][w] = i番目までの色を使って予算w以下で得られる最大効用
    dp = [[-1] * (X + 1) for _ in range(num_colors + 1)]
    dp[0][0] = 0
    
    for i in range(num_colors):
        color = color_list[i]
        color_table = color_dp[color]
        
        for w in range(X + 1):
            if dp[i][w] == -1:
                continue
            
            # この色を使わない場合
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])
            
            # この色を使う場合
            for cost in range(X + 1):
                if w + cost <= X and color_table[cost] != -1:
                    new_utility = dp[i][w] + color_table[cost]
                    dp[i + 1][w + cost] = max(dp[i + 1][w + cost], new_utility)
    
    # 各色数について最大満足度を計算
    max_satisfaction = 0
    
    for used_colors in range(num_colors + 1):
        # used_colors個の色を使う場合の最大効用を求める
        # これは組み合わせ最適化なので、別のアプローチが必要
        pass
    
    # より効率的なアプローチ: 各予算・各色数の組み合わせでDPを実行
    # dp[colors_used][budget] = その条件での最大効用
    max_colors = min(num_colors, 64)  # メモリ制限を考慮
    
    dp = [[-1] * (X + 1) for _ in range(max_colors + 1)]
    dp[0][0] = 0
    
    for color in color_list:
        color_table = color_dp[color]
        # 逆順で更新（同じ色を複数回使わないため）
        new_dp = [row[:] for row in dp]
        
        for colors_used in range(max_colors):
            for budget in range(X + 1):
                if dp[colors_used][budget] == -1:
                    continue
                
                # この色の商品を追加
                for cost in range(1, X + 1):
                    if budget + cost <= X and color_table[cost] != -1:
                        new_colors = colors_used + 1
                        if new_colors <= max_colors:
                            new_utility = dp[colors_used][budget] + color_table[cost]
                            new_dp[new_colors][budget + cost] = max(
                                new_dp[new_colors][budget + cost], new_utility
                            )
        
        dp = new_dp
    
    # 最大満足度を計算
    max_satisfaction = 0
    for colors_used in range(max_colors + 1):
        for budget in range(X + 1):
            if dp[colors_used][budget] != -1:
                satisfaction = dp[colors_used][budget] + colors_used * K
                max_satisfaction = max(max_satisfaction, satisfaction)
    
    return max_satisfaction

print(solve())