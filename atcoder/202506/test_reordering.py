# I - Reordering のテスト

import subprocess
import sys

def test_reordering():
    test_cases = [
        ("aa", 2),      # "a" と "aa"
        ("aba", 8),     # 正しい値に修正
        ("abc", 15),    # すべての非空部分列の順列
    ]
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        print(f"テストケース {i}: 入力='{input_str}', 期待値={expected}")
        
        # Pythonスクリプトを実行
        result = subprocess.run(
            [sys.executable, "c:/try/atcoder/202506/reordering.py"],
            input=input_str,
            text=True,
            capture_output=True
        )
        
        if result.returncode != 0:
            print(f"エラー: {result.stderr}")
            continue
            
        actual = int(result.stdout.strip())
        print(f"実際の出力: {actual}")
        
        if actual == expected:
            print("✓ 正解")
        else:
            print("✗ 不正解")
        print()

if __name__ == "__main__":
    test_reordering()