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
        if word not in self.sounds:
            self.sounds.append(word)
        else:
            print("WORD ALREADY TAUGHT\n")
        self.reduce_boredom()
    def feed(self):
        self.reduce_hunger()
    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)
        print("\nHunger reduced")
    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
        print("\nBoredom reduced")
class Dog1(Pet):
    def __init__(self, name="Pluto"):
        Pet.__init__(self, name="Bruno")
        self.sound = "Bow"
class Dog2(Pet):
    def __init__(self, name="Pluto"):
        Pet.__init__(self, name="Pluto")
        self.sound = "Bow"
class Doog(Dog1,Dog2):
    def __init__(self, name="Pluto"):
        Dog1.__init__(self, name="Pluto")
        self.sound = "Bow"

class Cat(Pet):
    def __init__(self, name="Snowy"):
        Pet.__init__(self, name="Snowy")
        self.sound = "Meew"
class Parrot(Pet):
    def __init__(self, name="Rio"):
        Pet.__init__(self, name="Rio")
        self.sound = "Kee"
pick = int(input("SELECT THE PET\n1)Puppy\n2)Kitten\n"))
if (pick == 2):
    p1 = Cat()
    #p2 = Dog()
elif (pick == 1):
   #p2 = Cat()
    p1 = Doog()
elif (pick==3):
    p1=Parrot()
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
    #p2.clock_tick()
    x=input("DO YOU WANT TO CONTINUE(n/y)")
