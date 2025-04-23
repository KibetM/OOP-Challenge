ALL_TRICKS=[]

class Pet:
    def __init__(self,name, hunger=10, energy=5, happiness=0):
        self.name=name
        self.hunger=hunger
        self.energy=energy
        self.happiness=happiness
        print(f"Creating a pet:{self.name}")

    def eat(self):
        self.hunger=max(self.hunger-3,0)
        self.happiness=min(self.happiness+1, 10)
        print(f"{self.name} is eating...")

    def sleep(self):
        self.energy=min(self.energy+5, 10)
        print(f"{self.name} is sleeping...")

    def play(self):
        self.energy=max(self.energy-2, 10)
        self.happiness=min(self.happiness+2, 10)
        self.hunger=min(self.hunger+1, 10)
        print(f"{self.name} is playing")

    def get_status(self):
        print(f"self.name:{self.name}")
        print(f"self.hunger:{self.hunger}")
        print(f"self.energy:{self.energy}")
        print(f"self.happiness:{self.happiness}")

    def train(self,trick):
        ALL_TRICKS.append(trick)

    def show_tricks(self):
        print(ALL_TRICKS)