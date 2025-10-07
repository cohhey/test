# デバッグ用: 具体的な計算
def debug_jump(x1, y1, x2, y2):
    print(f"From ({x1},{y1}) to ({x2},{y2})")
    print(f"x1+y1={x1+y1}, x2+y2={x2+y2}")
    print(f"x1-y1={x1-y1}, x2-y2={x2-y2}")
    
    if (x1 + y1) % 2 != (x2 + y2) % 2:
        print("到達不可能（奇偶性が異なる）")
        return 0
    
    u1, v1 = x1 + y1, x1 - y1
    u2, v2 = x2 + y2, x2 - y2
    
    u_dist = abs(u2 - u1) // 2
    v_dist = abs(v2 - v1) // 2
    
    print(f"u距離: {u_dist}, v距離: {v_dist}")
    print(f"最大値: {max(u_dist, v_dist)}")
    return max(u_dist, v_dist)

# テスト
debug_jump(0, 0, 1, 3)
print("---")
debug_jump(0, 0, 5, 6)
print("---")
debug_jump(1, 3, 5, 6)