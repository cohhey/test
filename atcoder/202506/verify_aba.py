# ABAの詳細検証

def verify_aba():
    S = "aba"
    
    # 可能な部分列
    # 位置: 0=a, 1=b, 2=a
    subsequences = []
    
    # 長さ1
    subsequences.append("a")  # 位置0
    subsequences.append("b")  # 位置1
    subsequences.append("a")  # 位置2
    
    # 長さ2
    subsequences.append("ab") # 位置0,1
    subsequences.append("aa") # 位置0,2
    subsequences.append("ba") # 位置1,2
    
    # 長さ3
    subsequences.append("aba") # 位置0,1,2
    
    print("すべての部分列:")
    for i, subseq in enumerate(subsequences):
        print(f"{i+1}: {subseq}")
    
    # 各部分列から作れる異なる順列
    distinct_strings = set()
    
    for subseq in subsequences:
        from itertools import permutations
        perms = set(permutations(subseq))
        for perm in perms:
            distinct_strings.add(''.join(perm))
    
    print(f"\n異なる文字列の総数: {len(distinct_strings)}")
    print("異なる文字列:")
    for s in sorted(distinct_strings):
        print(f"  {s}")

if __name__ == "__main__":
    verify_aba()