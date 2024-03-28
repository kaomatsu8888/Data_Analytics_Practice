# Appleの文字を1文字ずつ取り出して、pのときはスキップする
for ch in "Apple":
    print(ch)
    if ch == "p":
        break
        
print(f"{ch}最後の出力")
