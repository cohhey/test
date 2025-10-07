# AtCoder オンラインショッピング問題
# 入力の読み込み: N（商品の種類数）、S（送料無料の閾値）、K（送料）を読み込む
# 商品の合計金額計算: 各商品について価格×個数を計算し、すべて合計する
# 送料の判定: 合計金額がS円以上なら送料0円、未満ならK円
# 最終支払金額: 商品合計金額 + 送料

# 入力を読み込む
N, S, K = map(int, input().split())

# 商品の合計金額を計算
total_cost = 0
for i in range(N):
    P, Q = map(int, input().split())
    total_cost += P * Q

# 送料を計算
if total_cost >= S:
    shipping_cost = 0
else:
    shipping_cost = K

# 最終的な支払金額を計算
final_cost = total_cost + shipping_cost

# 結果を出力
print(final_cost)