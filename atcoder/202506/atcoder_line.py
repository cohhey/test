# A - AtCoder Line の解答

# 入力を読み込む
N, X, Y, Z = map(int, input().split())

# XからYへの移動経路にZが含まれるかを判定
if X < Y:
    # 上り列車（X → X+1 → X+2 → ... → Y）
    if X < Z < Y:
        print("Yes")
    else:
        print("No")
else:
    # 下り列車（X → X-1 → X-2 → ... → Y）
    if Y < Z < X:
        print("Yes")
    else:
        print("No")