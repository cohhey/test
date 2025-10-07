# F - Palindromic in Both Bases
# 十進法とA進法の両方で回文となる数の総和を求める

def to_base(n, base):
    """数値nをbase進法の数字リストに変換"""
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    return digits[::-1]

def is_palindrome_base(n, base):
    """数値nがbase進法で回文かどうか判定"""
    digits = to_base(n, base)
    return digits == digits[::-1]

def is_palindrome_decimal(n):
    """数値nが十進法で回文かどうか判定"""
    s = str(n)
    return s == s[::-1]

def solve(A, N):
    total = 0
    
    # すべての数について十進法と A進法 両方で回文かチェック
    # 効率化のため、十進法回文のみを生成してからA進法回文かチェック
    
    # 1桁の回文 (1-9)
    for i in range(1, min(10, N + 1)):
        if is_palindrome_base(i, A):
            total += i
    
    if N < 10:
        return total
    
    # 2桁以上の回文を系統的に生成
    for digits in range(2, 13):  # 最大12桁
        start = 10 ** (digits - 1)
        if start > N:
            break
        
        if digits % 2 == 0:
            # 偶数桁回文
            half = digits // 2
            for i in range(10 ** (half - 1), 10 ** half):
                s = str(i)
                palindrome_str = s + s[::-1]
                num = int(palindrome_str)
                if num > N:
                    break
                if is_palindrome_base(num, A):
                    total += num
        else:
            # 奇数桁回文
            half = digits // 2
            for i in range(10 ** (half - 1), 10 ** half):
                for middle in range(10):
                    s = str(i)
                    palindrome_str = s + str(middle) + s[::-1]
                    num = int(palindrome_str)
                    if num > N:
                        break
                    if is_palindrome_base(num, A):
                        total += num
    
    return total

# 入力を受け取る
A = int(input())
N = int(input())

# 答えを出力
print(solve(A, N))

# 入力を受け取る
A = int(input())
N = int(input())

# 答えを出力
print(solve(A, N))