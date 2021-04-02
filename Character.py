class Character(object):

    def __init__(self, name="Unknown",health=100,attack=0,defense=0,level=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level

    def get_info_string(self):
        string = f"{self.name} is a {self.__class__.__name__} and he/she is now at {self.level} level"
        #string = f"{self.name} is a {self.__class__.__name__} and they are {self.age} years old"
        return string


    def print_info(self):
        print(self.get_info_string())

class Monster(object):
    def __init__(self,name="Otaku Goblin",health=100,attack=25,level=1,defense=10):
        self.name=name
        self.health=health
        self.attack=attack
        self.defense=defense
        self.level=level
        self.money = 100
        print(open('battle/battleMonster1.txt').read())
class Monster2(Monster):
    def __init__(self):
        super(Monster2, self).__init__(name='Elves',health=150,attack=30,defense=15,level=2)
        print(open('battle/battleMonster2.txt').read())
class Monster3(Monster):
    def __init__(self):
        super(Monster3, self).__init__(name='Robber',health=175,attack=30,defense=5,level=3)
        print(open('battle/battleMonster3.txt').read())
class Monster4(Monster):
    def __init__(self):
        super(Monster4, self).__init__(name='Magician', health=100, attack=40, defense=0,level=4)
        self.money=200
        print(open('battle/battleMonster4.txt').read())
class Monster5(Monster):
    def __init__(self):
        super(Monster5, self).__init__(name='Skeleton', health=400, attack=40, defense=0,level=5)
        print(open('battle/battleMonster5.txt').read())
class Samurai (Character):
    def __init__(self):
        super(Samurai, self).__init__(name="Takasugi Shinsuke",health=500,attack=90,defense=30,level=6)
        self.money=0
        print(open('battle/battleMonster6.txt').read())
class Ashina(Character):
    def __init__(self):
        super(Ashina, self).__init__(name="Ashina Isshin",health=500,attack=100,defense=30,level=7)
        self.money=0
        print(open('battle/battleMonster7.txt').read())

class Player(Character):
    def __init__(self,name="Katsura",health=100,attack=10,defense=0,level=1):
        super(Player, self).__init__(name,health,attack,defense,level)
        self.money = 100
        self.maxHealth=200
    def ifLevelUp(self):
        #100Xp is a level, level starts from level 1
        while True:
            if (self.exp>=100*self.level):
                self.level+=1
            else:
                break
    def suicide(self):
        self.health=0
        return 0

class Dragon(Monster):
    def __init__(self,name="Boss:Dragon",health=1000,attack=100,level=25,defense=50):
        super().__init__(name,health,attack,defense)
        self.level=level