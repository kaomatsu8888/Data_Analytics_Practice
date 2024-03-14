#3-7 次のコードを実行した結果｛4 ,3, 2, 1｝が表示されるとき、空欄に入る適切なコードを選択しなさい
stack = [1, 2, 3, 4]
data = []
print(data)
while stack:
    print(stack)
    data.append(stack.pop()) # satck.pop()はリストの最後の要素を出し、その要素をリストから削除する.append()はリストの最後に要素を追加する
print(data)

