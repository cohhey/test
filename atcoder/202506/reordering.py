# I - Reordering の解答

from collections import Counter

MOD = 998244353

def solve():
    S = input().strip()
    n = len(S)
    
    # 各文字の出現回数をカウント
    char_count = Counter(S)
    chars = list(char_count.keys())
    
    # 前計算：階乗とその逆元
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD
    
    def multinomial(total, counts):
        """多項式係数を計算"""
        if total == 0:
            return 1
        result = fact[total]
        for cnt in counts:
            result = (result * inv_fact[cnt]) % MOD
        return result
    
    # DPで解く
    # dp[使った文字数] = その文字数で作れる異なる文字列の数
    # 実際には各文字の使用個数の組み合わせを管理
    
    result = 0
    
    # 各可能な部分列について
    # 文字の組み合わせを全列挙
    def dfs(char_idx, current_counts, total_used):
        nonlocal result
        
        if char_idx == len(chars):
            if total_used > 0:
                # この組み合わせで作れる異なる文字列の数
                ways = multinomial(total_used, current_counts)
                result = (result + ways) % MOD
            return
        
        char = chars[char_idx]
        max_count = char_count[char]
        
        # この文字を0個からmax_count個まで使う
        for use_count in range(max_count + 1):
            current_counts.append(use_count)
            dfs(char_idx + 1, current_counts, total_used + use_count)
            current_counts.pop()
    
    dfs(0, [], 0)
    print(result)

solve()