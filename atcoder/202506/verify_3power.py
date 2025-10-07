# 検証用プログラム
def verify(A, expected_M):
    total = sum(3**a for a in A)
    print(f"A = {A}")
    print(f"Sum = {' + '.join(f'3^{a}' for a in A)} = {' + '.join(str(3**a) for a in A)} = {total}")
    print(f"Expected: {expected_M}, Actual: {total}, Match: {total == expected_M}")
    print()

# テストケース1
verify([1, 1], 6)

# テストケース2  
verify([4, 2, 2, 0], 100)

# テストケース3の一部確認
A3 = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0]
print(f"テストケース3: N={len(A3)}")
print("3の累乗:")
for i in range(11):
    print(f"3^{i} = {3**i}")
print()

# 59048の検証
total = sum(3**a for a in A3)
print(f"計算結果: {total}")
print(f"期待値: 59048")
print(f"一致: {total == 59048}")