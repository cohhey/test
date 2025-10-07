# F - Just K の解答

# 全探索: 2^N通りの文字列の選び方をすべて試す
# 文字カウント: 選んだ文字列について各文字の出現回数をカウント
# 条件チェック: ちょうどK回出現する文字の数をカウント
# 最大値更新: 全ての選び方の中で最大値を記録

from itertools import combinations

def solve():
    N, K = map(int, input().split())
    strings = []
    for _ in range(N):
        strings.append(input().strip())
    
    max_count = 0
    
    # すべての可能な文字列の選び方を試す（ビット全探索）
    for bits in range(1 << N):
        selected_strings = []
        for i in range(N):
            if bits & (1 << i):
                selected_strings.append(strings[i])
        
        # 選んだ文字列が0個の場合はスキップ
        if len(selected_strings) == 0:
            continue
        
        # 各文字の出現回数をカウント
        char_count = {}
        for s in selected_strings:
            for char in s:
                char_count[char] = char_count.get(char, 0) + 1
        
        # ちょうどK回出現する文字の数をカウント
        exactly_k_count = 0
        for char, count in char_count.items():
            if count == K:
                exactly_k_count += 1
        
        max_count = max(max_count, exactly_k_count)
    
    return max_count

print(solve())