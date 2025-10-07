# G - String Rotation
# 文字列の連続部分文字列を左に1つ巡回シフトして辞書順最小の結果を求める

def solve_case(s):
    n = len(s)
    min_result = s  # 初期状態
    
    # 全ての可能な範囲[l, r]について試す
    for l in range(n):
        for r in range(l, n):
            # 範囲[l, r]を左に1つ巡回シフト
            # s[l]を範囲の最後に移動
            if l == r:
                # 長さ1の範囲では変化なし
                result = s
            else:
                # s[l:r+1]の最初の文字を最後に移動
                substring = s[l:r+1]
                rotated = substring[1:] + substring[0]
                result = s[:l] + rotated + s[r+1:]
            
            # 辞書順で比較して最小を更新
            if result < min_result:
                min_result = result
    
    return min_result

# 入力を受け取る
T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()
    print(solve_case(S))