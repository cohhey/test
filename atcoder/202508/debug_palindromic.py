# デバッグ用プログラム
def to_base(n, base):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    return digits[::-1]

def is_palindrome_base(n, base):
    digits = to_base(n, base)
    return digits == digits[::-1]

def is_palindrome_decimal(n):
    s = str(n)
    return s == s[::-1]

# A=8, N=1000で条件を満たす数を探す
A = 8
N = 1000
valid_numbers = []

for i in range(1, N + 1):
    if is_palindrome_decimal(i) and is_palindrome_base(i, A):
        valid_numbers.append(i)
        print(f"{i}: 10進法={i}, 8進法={''.join(map(str, to_base(i, A)))}")

print(f"条件を満たす数: {valid_numbers}")
print(f"個数: {len(valid_numbers)}")
print(f"総和: {sum(valid_numbers)}")