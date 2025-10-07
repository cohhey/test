# F - Slot Strategy 2 (Easy) の解答

def solve():
    M = int(input())
    S = [input().strip() for _ in range(3)]
    
    min_time = float('inf')
    
    # 全ての可能な文字について試す
    for char in '0123456789':
        # この文字で全てのリールを揃えられるかチェック
        possible_times = [[] for _ in range(3)]
        all_possible = True
        
        for reel in range(3):
            for t in range(M):
                if S[reel][t] == char:
                    possible_times[reel].append(t)
            
            if not possible_times[reel]:
                all_possible = False
                break
        
        if not all_possible:
            continue
        
        # 全てのリールでこの文字を表示できる組み合わせを試す
        for t1 in possible_times[0]:
            for t2 in possible_times[1]:
                for t3 in possible_times[2]:
                    # 全てのリールを止める時間は、最後に止めるリールの時間
                    total_time = max(t1, t2, t3)
                    min_time = min(min_time, total_time)
    
    if min_time == float('inf'):
        print(-1)
    else:
        print(min_time)

solve()