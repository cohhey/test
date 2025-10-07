# 商品購入と送料の計算問題
# N種類の商品を購入、送料の条件によって総支払額を計算

# 入力を受け取る
N, S, K = map(int, input().split())

# 商品の合計金額を計算
total_cost = 0
for i in range(N):
    P, Q = map(int, input().split())
    total_cost += P * Q

# 送料を計算
if total_cost >= S:
    shipping_fee = 0
else:
    shipping_fee = K

# 総支払額を計算
total_payment = total_cost + shipping_fee

print(total_payment)