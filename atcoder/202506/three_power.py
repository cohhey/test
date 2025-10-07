# D - 3^A の解答

def solve():
    M = int(input())
    
    # 貪欲法: 大きい3の累乗から順に使用
    # 3^10 = 59049 が最大使用可能
    A = []
    remaining = M
    
    # 大きいものから順に使用
    for i in range(10, -1, -1):
        power = 3**i
        count = remaining // power
        
        # count が 0 でない場合のみ追加
        for _ in range(count):
            A.append(i)
        
        remaining %= power
    
    # 結果を出力
    N = len(A)
    print(N)
    if N > 0:
        print(*A)

solve()