default_name = "Taro" # グローバル変数

def hello(name=default_name): # デフォルト引数
    return f"Hello, {name}!"  # f-string

def hello2(name=None): # name引数がデフォルト値のNoneになる
    if name is None: # Noneの場合
        name = default_name # グローバル変数を使う
    return f"Hello, {name}!" #

default_name = "Hanako"
print(hello(), hello2()) # "Hello, Taro!" "Hello, Hanako!"
