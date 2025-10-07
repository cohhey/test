# デバッグ用：詳細な動作確認
def debug_solve(s):
    n = len(s)
    print(f"Original: {s}")
    min_result = s
    best_operation = None
    
    for l in range(n):
        for r in range(l, n):
            if l == r:
                result = s
            else:
                substring = s[l:r+1]
                rotated = substring[1:] + substring[0]
                result = s[:l] + rotated + s[r+1:]
            
            print(f"Range [{l},{r}]: {s[l:r+1]} -> {result}")
            
            if result < min_result:
                min_result = result
                best_operation = (l, r)
    
    print(f"Best: {min_result} (range {best_operation})")
    return min_result

# "atcoder"の例で詳細確認
debug_solve("atcoder")