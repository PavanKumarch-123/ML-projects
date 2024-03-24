class car:
    def __init__(self, name, color):
        self.n = name
        self.c = color
    def drive(self):
        print(f"{self.n} {self.c} is driving by me")
