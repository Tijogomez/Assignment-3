from random import randrange
class Pet():
    boredom_decrement = 3
    hunger_decrement = 4
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = [""]
    def __init__(self, name="Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]
    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1
    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"
    def __str__(self):
        state = "I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        return state
    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()
    def teach(self):
        word = input("ENTER THE WORD TO BE TAUGHT:")
        self.sounds.append(word)
        self.reduce_boredom()
    def feed(self):
        self.reduce_hunger()
    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)
        print("\nHunger reduced")
    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
        print("\nBoredom reduced")
class Parrot(Pet):
    sound = []
    def __init__(self, name="Pepe"):
        Pet.__init__(self, name="Pepe")
        self.sound = "keee"
class Monkey(Pet):
    sound = []
    def __init__(self, name="Jack"):
        Pet.__init__(self, name="Jack")
        self.sound = "howwl"
pick = int(input("SELECT THE PET\n1)Birdie\n2)Mammal\n"))
if (pick == 1):
    p1 = Parrot()
elif (pick == 2):
    p1 = Monkey()
else:
    print("WRONG INPUT")
x="y"
while x=="y" or x=="Y":
    cmd = int(input("COMMANDS:\n1)Greet\n2)Teach\n3)Feed\n"))
    print(p1)
    if (cmd == 1):
        p1.hi()
    elif (cmd == 2):
        p1.teach()
    elif (cmd == 3):
        p1.feed()
    p1.clock_tick()
    x=input("DO YOU WANT TO CONTINUE(x/y)")

