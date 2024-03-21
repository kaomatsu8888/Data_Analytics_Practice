class Duck: # Duckクラスを定義
    family = "Anatidae" # クラス変数familyを定義

    #特殊メソッド__init__を定義
    def __init__(self): # インスタンス変数birdsongを定義
        self.birdsong = "quack" # インスタンス変数birdsongを初期化
    
    # show_faimilyメソッドを定義
    def show_family(self): # クラス変数familyを返す
        return f"Ducks belong to the family {self.family}" # クラス変数familyを返す

duck = Duck() # Duckクラスのインスタンスを生成
