# D - Unvarnished Report
# 文字列の読み込み: 2つの文字列SとTを読み込む
# 完全一致チェック: SとTが完全に等しい場合は0を出力
# 文字単位の比較: 各位置で文字を比較し、最初に異なる位置を探す
# 範囲外処理: 片方の文字列が短い場合も異なるとみなす

# 入力を読み込む
S = input().strip()
T = input().strip()

# 文字列が等しいかチェック
if S == T:
    print(0)
else:
    # 最初に異なる位置を探す
    max_len = max(len(S), len(T))
    
    for i in range(max_len):
        # i番目の文字を比較（0-indexedなので、出力は1-indexedにする）
        s_char = S[i] if i < len(S) else None
        t_char = T[i] if i < len(T) else None
        
        # 文字が異なるか、片方にのみ存在する場合
        if s_char != t_char:
            print(i + 1)  # 1-indexedで出力
            break