# G - ABC Transform の解答

def solve():
    S = input().strip()
    Q = int(input())
    
    # 文字の変換ルール
    transform = {'A': 'BC', 'B': 'CA', 'C': 'AB'}
    
    def find_char(s, t, k):
        """文字列sをt回変換した結果のk番目の文字を求める（1-indexed）"""
        if t == 0:
            return s[k - 1]
        
        # 1段階前の変換結果のどの位置に対応するかを逆算
        pos = 1
        for char in s:
            transformed = transform[char]
            
            # この文字の変換結果の長さを計算
            if t == 1:
                char_len = len(transformed)
            else:
                # t > 1の場合、再帰的に計算
                char_len = get_length(transformed, t - 1)
                if char_len > 10**18:
                    char_len = 10**18  # 制限
            
            if pos <= k <= pos + char_len - 1:
                # k番目の文字はこの文字の変換結果内にある
                return find_char(transformed, t - 1, k - pos + 1)
            
            pos += char_len
        
        # ここに到達することはないはず
        return 'A'
    
    def get_length(s, t):
        """文字列sをt回変換した結果の長さを求める"""
        if t == 0:
            return len(s)
        
        if t > 50:  # 長さが大きすぎる場合
            return 10**18
        
        total = 0
        for char in s:
            transformed = transform[char]
            char_len = get_length(transformed, t - 1)
            total += char_len
            if total > 10**18:
                return 10**18
        
        return total
    
    # クエリ処理
    for _ in range(Q):
        t, k = map(int, input().split())
        result = find_char(S, t, k)
        print(result)

solve()