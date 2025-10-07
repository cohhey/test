def fmt(s):
    return f"{s:03}"

s=int(input())
if s<=42:
    print ("AGC"+fmt(s))
else:
    print("AGC"+fmt(s+1))
