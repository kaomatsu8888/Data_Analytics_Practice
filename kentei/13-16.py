def concat(arg1, arg2, sep="/"): # "/"は
    return sep.join([arg1, arg2]) # sep.join()はsepで区切って連結する.separate

words = ["foo", "bar"] # 2つの文字列をリストに格納。リストは[]で囲む
options = {"sep": "_"} # sepをキーにして"_"を値に持つ辞書を作成。タプルは{}で囲む
print(concat(*words, **options)) # "foo _ bar" concat()関数にwordsリストとoptions辞書を展開して渡す
