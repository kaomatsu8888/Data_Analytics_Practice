glb = 0 # グローバル変数

def func1(): # グローバル変数を参照する関数
    glb = 1 # ローカル変数

def func2(): # グローバル変数を変更する関数
    global glb # グローバル変数を参照する
    glb = 5 # グローバル変数を変更する

print(glb) # 0が出力される
func1()
print(glb) # 0が出力される
func2()
print(glb) # 5が出力される
