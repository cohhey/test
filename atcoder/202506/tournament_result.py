# C - Tournament Result の解答

def solve():
    N = int(input())
    A = []
    for _ in range(N):
        row = input().strip()
        A.append(row)
    
    # 矛盾をチェック
    for i in range(N):
        for j in range(N):
            if i == j:
                # 対角線要素は'-'でなければならない
                if A[i][j] != '-':
                    return "incorrect"
            else:
                # 対戦結果の整合性をチェック
                if A[i][j] == 'W':
                    # i が j に勝った場合、j は i に負けていなければならない
                    if A[j][i] != 'L':
                        return "incorrect"
                elif A[i][j] == 'L':
                    # i が j に負けた場合、j は i に勝っていなければならない
                    if A[j][i] != 'W':
                        return "incorrect"
                elif A[i][j] == 'D':
                    # i が j と引き分けた場合、j も i と引き分けていなければならない
                    if A[j][i] != 'D':
                        return "incorrect"
                else:
                    # 無効な文字
                    return "incorrect"
    
    return "correct"

print(solve())