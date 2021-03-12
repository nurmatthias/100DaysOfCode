class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("inhale... exhale...")

class Fish(Animal):

    def __init__(self) -> None:
        super().__init__()

    def swim(self):
        print("moving in water")
    
    def breathe(self):
        super().breathe()
        print("doing this unserwater")


nemo = Fish()
nemo.swim()
nemo.breathe()

print(nemo.num_eyes)
