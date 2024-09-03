
class Bird:
    def __init__(self):
        print("Bird is Ready")
    
    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("swim Faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is Ready")

    def whoisthis(self):
        print("Penguin")
    
    def swim(self):
        print("Penguin is swimming")

peggy=Penguin()
peggy.swim()