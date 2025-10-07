# 回転寿司シミュレーション問題
# N人の人とM個の寿司、美食度と美味しさの条件で誰が寿司を取るかを判定

# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))  # 各人の美食度
M = int(input())
B = list(map(int, input().split()))  # 各寿司の美味しさ

# 各寿司について誰が食べるかを判定
for j in range(M):
    sushi_deliciousness = B[j]
    taken = False
    
    # 人1からNまで順番に寿司の前を通る
    for i in range(N):
        person_gourmet = A[i]
        
        # 美味しさが美食度以上なら寿司を取る
        if sushi_deliciousness >= person_gourmet:
            print(i + 1)  # 人の番号は1から始まる
            taken = True
            break
    
    # 誰も取らなかった場合
    if not taken:
        print(-1)