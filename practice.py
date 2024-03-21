class Duck:
    def __init__(self):
        self.birdsong = "quack"

    def change_birdsong(self, birdsong):
        self.birdsong = birdsong

    def show_birthplace(self):
        print(self.birdsong)
        self.change_birdsong("ga-ga")
        print(self.birdsong)

Duck().show_birthplace()
