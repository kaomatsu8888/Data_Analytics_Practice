class Duck: # Duckクラスを定義
    def __init__(self): # インスタンス変数birdsongを定義
        self.birdsong = "quack" # インスタンス変数birdsongを初期化

    def sing(self): # singメソッドを定義
        birdsong = "ga-ga-" # ローカル変数birdsongを定義
        print(birdsong) 
        print(self.birdsong)
        self.birdsong = "coin"
        print(self.birdsong)
        print(birdsong)

duck = Duck()
duck.sing()

# 出力結果
# ga-ga-
# quack
# coin
# ga-ga-
