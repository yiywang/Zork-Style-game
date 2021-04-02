import Character
import time
import Map
class Event(object):
    def __init__(self):
        self.starStr="********************************************************\n"
    def play(self):
        nom = input("Enter your name~ （Default: Katsura）\n")
        if nom =='':
            player=Character.Player(name="Katsura",health=200,attack=20,defense=10,level=1)
        else:
            player = Character.Player(name=nom, health=200, attack=20, defense=10, level=1)
        self.spawnEvent(player)  # start of the game
        self.printStatus(player)
        self.crossingEvent(3)  # 出生点 Spawn site
        print(open('crossing/crossing1_2_3.txt').read())
        routeFlag = input("Your decision:")
        mapServer = Map.Map()
        while (True):
            if (routeFlag=='-2'):
                print("-------------Exit Game--------------")
                break
            if (routeFlag == '-1'):  # 二周目
                nom = input("Welcome back! Winner! Enter your name~ （Default: Katsura)")
                if nom == '':
                    player = Character.Player(name="Katsura", health=300, attack=30, defense=15, level=2)
                else:
                    player = Character.Player(name=nom,  health=300, attack=30, defense=15, level=2)
                self.crossingEvent(3)  # 出生点
                time.sleep(1)
                print(open('crossing/crossing1_2_3.txt').read())
                routeFlag = input("Your decision:")

            if (routeFlag == '0'):
                player = Character.Player(name="Katsura", health=200, attack=20, defense=10, level=1)
                self.spawnEvent(player)
                print(open('crossing/crossing1_2_3.txt').read())
                routeFlag = input("Your decision:")
            if (routeFlag == '1'):
                mapServer.location(int(routeFlag))
                # Event 1-1 Fruit Tree,attack+
                self.eatFruits(player,1)
                # Event 1-2 Battle:Otaku Goblin level1
                monster = Character.Monster()
                win = self.battle(player, monster)
                self.printStatus(player)
                if (win == True):
                    # Event 1-3 Mysterious Box
                    self.goldBox(player,type=1)
                    # Event 1-4:Merchant level1
                    self.purchase(player,1)
                    # Branch 1-4-5 Format:from1 to 4 or 5 In this order.
                    mapServer.location(int(routeFlag))
                    routeFlag=mapServer.switch(1,4,5)
                else:  # If died in the battle 1-2
                    routeFlag = '0'

            elif (routeFlag == '2'):
                mapServer.location(int(routeFlag))
                #Event 2-1 Merchant lv1
                self.purchase(player,1)
                #Event 2-2 Gold Box+100
                self.goldBox(player,type=1)
                #Event 2-3 Monster lv1
                monster=Character.Monster()
                win = self.battle(player,monster)
                if win==False:
                    routeFlag='0'
                else:
                    #Event 2-4 Bomb box
                    flag = self.bombBoxEvent(player)
                    if flag == False:  # If killed by the bomb, back to the respawn point.
                        routeFlag = '0'
                    else:
                        #Event 2-5 Attack Fruit
                        self.eatFruits(player,type=1)
                        routeFlag = '6'

            elif (routeFlag == '3'):
                mapServer.location(int(routeFlag))
                #Event 3-1 Merchant lv1
                self.purchase(player,1)
                #Event 3-2 Monster lv1
                monster=Character.Monster()
                win=self.battle(player,monster)
                if win==False:
                    routeFlag='0'
                else:
                    #Event 3-3 Poisonous Fruit
                    self.eatFruits(player,type=3)
                    if player.health<=0:
                        routeFlag='0'
                    else:
                        #Branch Road 3-7-13
                        mapServer.location(int(routeFlag))
                        routeFlag=routeFlag = mapServer.switch(3, 7, 13)

            if (routeFlag == '4'):
                mapServer.location(int(routeFlag))
                # Event 4-1 Fruit Tree Defense+
                self.eatFruits(player,2)

                # Event 4-2 Monster level3
                monster = Character.Monster3()
                win = self.battle(player, monster)
                if (win == True):
                    # Branch road 4-10-11
                    mapServer.location(int(routeFlag))
                    routeFlag = mapServer.switch(4, 10, 11)
                else:
                    routeFlag = '0'

            elif (routeFlag == '5'):
                mapServer.location(int(routeFlag))
                #Event 5-1 Bomb box
                flag = self.bombBoxEvent(player)
                if flag == False:  # If killed by the bomb, back to the respawn point.
                    routeFlag = '0'
                else:
                    # Event 5-2 Campfire
                    self.camping(player)
                    # Event 5-3 Poisonous Fruit
                    self.eatFruits(player, 3)
                    if player.health <= 0:
                        routeFlag = '0'
                    else:
                        # Event 5-4 Attack+
                        self.eatFruits(player, 1)
                        # Event 5-5 Merchant level2
                        self.purchase(player,2)
                        # Event 5-6 Monster level4
                        monster = Character.Monster4()
                        win = self.battle(player, monster)
                        if (win == False):
                            routeFlag = '0'
                        else:
                            mapServer.location(int(routeFlag))
                            # Branch Road 5-12-16
                            routeFlag = mapServer.switch(5, 12, 16)

            if (routeFlag == '6'):
                mapServer.location(int(routeFlag))
                #Event 6-1 Camping
                self.camping(player)
                #Event 6-2 Defense Fruit
                self.eatFruits(player,type=2)
                #Event 6-3 Monster lv4
                monster=Character.Monster4()
                win=self.battle(player,monster)
                if win==False:
                    routeFlag='0'
                else:
                    mapServer.location(int(routeFlag))
                    #Branch Road 6-8-9
                    routeFlag=mapServer.switch(6,8,9)

            if (routeFlag == '7'):
                mapServer.location(int(routeFlag))
                #Event 7-1
                self.eatFruits(player,type=1)
                #Event 7-2 Monster lv2
                monster=Character.Monster2()
                win=self.battle(player,monster)
                if win==False:
                    routeFlag='0'
                else:#Road 7-6
                    routeFlag = '6'

            if (routeFlag == '8'):  # 这是出口之一
                mapServer.location(int(routeFlag))
                # Event 8-2 Merchant lv3
                self.purchase(player,3)
                # Event 8-3 Camping
                self.camping(player)
                # Event 8-4 Dragon
                dragon = Character.Dragon()
                win = self.battle(player, dragon)
                if win == False:
                    routeFlag = '0'
                else:
                    routeFlag = self.win()
            if (routeFlag == '9'):  # 这是出口之一
                mapServer.location(int(routeFlag))
                #Event 9-1 Gold Box+500
                self.goldBox(player,type=2)
                #Event 9-2 Merchantlv2
                self.purchase(player,2)
                #Event 9-3 Monster lv5
                monster=Character.Monster5()
                win=self.battle(player,monster)
                if win==False:
                    routeFlag='0'
                else:
                    routeFlag=self.win()

            if (routeFlag == '10'):
                mapServer.location(int(routeFlag))
                #Event 10-1 Monster level2
                monster=Character.Monster2()
                win = self.battle(player, monster)
                if (win == False):
                    routeFlag = '0'
                else:
                    #Event 10-2 Camping
                    self.camping(player)
                    #Event 10-3 Monster level4
                    monster=Character.Monster4()
                    win = self.battle(player, monster)
                    if (win == False):
                        routeFlag = '0'
                    else:
                        # Event 10-4 attack fruit
                        self.eatFruits(player,type=1)
                        # Event 10-5 Bomb Box
                        flag = self.bombBoxEvent(player)
                        if flag == False:  # If killed by the bomb, back to the respawn point.
                            routeFlag = '0'
                        else:
                            # Event 10-6 Merchant level2
                            self.purchase(player,2)
                            routeFlag = '17'
            if (routeFlag == '11'):  # 这是出口之一
                mapServer.location(int(routeFlag))
                # Event 11-1 Gold box
                self.goldBox(player,type=2)
                # Event 11-2 Merchant level3
                self.purchase(player,3)
                # Event 11-3 Campfire
                self.camping(player)
                # Event 11-4 Bomb box
                flag = self.bombBoxEvent(player)
                if flag == False:  # If killed by the bomb, back to the respawn point.
                    routeFlag = '0'
                else:
                    # Event 11-5 Final battle: Samurai
                    samurai = Character.Samurai()
                    print(open('battle/battleMonster6.txt').read())
                    win = self.battle(player, samurai)
                    self.printStatus(player)
                    if (win == True):
                        routeFlag=self.win()

            if (routeFlag == '12'):
                mapServer.location(int(routeFlag))
                #Event 12-1 Poison
                self.eatFruits(player,3)
                if player.health<=0:
                    routeFlag='0'
                else:
                    # Event 12-2 gold+100
                    self.goldBox(player, 1)
                    routeFlag = '17'
            if (routeFlag == '13'):
                mapServer.location(int(routeFlag))
                #Event 13-1 Def+
                self.eatFruits(player,type=2)
                #Event 13-2 Monster lv2
                monster=Character.Monster2()
                win=self.battle(player,monster)
                if win==False:
                    routeFlag='0'
                else:
                    #Event 13-3 Camping
                    self.camping(player)
                    #Event 13-4 Monster lv4
                    monster=Character.Monster4()
                    win=self.battle(player,monster)
                    if win==False:
                        routeFlag='0'
                    else:
                        #Event 13-5 Merchant lv2
                        self.purchase2(player)
                        mapServer.location(int(routeFlag))
                        #Branch road 13-14-15
                        routeFlag = mapServer.switch(13, 14, 15)


            if (routeFlag == '14'):
                mapServer.location(int(routeFlag))
                #Event 14-1 Monster level 5
                monster=Character.Monster5()
                win=self.battle(player,monster)
                if(win==False):
                    routeFlag='0'
                else:
                    #Event 14-2 Camping
                    self.camping(player)
                    mapServer.location(int(routeFlag))
                    #Branch 14-12-16
                    routeFlag = mapServer.switch(14, 12, 16)
            if (routeFlag == '15'):  # 这是出口之一
                mapServer.location(int(routeFlag))
                # Event 15-1 Monster level 5
                monster = Character.Monster5()
                win = self.battle(player, monster)
                if (win == False):
                    routeFlag = '0'
                else:
                    #Event 15-2 Poisonous Fruit
                    self.eatFruits(player,type=3)
                    if player.health <= 0:
                        routeFlag = '0'
                    else:
                        routeFlag = self.win()

            if (routeFlag == '16'):  # 这是出口之一
                mapServer.location(int(routeFlag))
                #Event 16-1 to 2 Attack fruit
                self.eatFruits(player,type=1)
                self.eatFruits(player, type=1)
            if (routeFlag == '17'):  # 这是出口之一
                mapServer.location(int(routeFlag))
                #Event 17-1 Monster lv5
                monster = Character.Monster5()
                win = self.battle(player, monster)
                if(win==False):
                    routeFlag='0'
                else:
                    # Event 17-2 Gold +500
                    self.goldBox(player, type=2)
                    # Event 17-3 Merchant lv3
                    self.purchase(player,3)
                    # Event 17-4 Camping
                    self.camping(player)
                    # Event 17-5 Boss:Ashina Isshin
                    AshinaIsshin = Character.Ashina()
                    win = self.battle(player, AshinaIsshin)
                    if(win==False):
                        routeFlag='0'
                    else:
                        routeFlag=self.win()


    def printStatus(self,p):
        str=self.starStr
        str+=f"Player {p.name} Status:\n"
        str+=f"Health:{p.health}/{p.maxHealth}\nAttack:{p.attack}\nDefense:{p.defense}\nCoin:{p.money} Gold"
        print(str)
        return 0

    def crossingEvent(self,x):
        str=self.starStr
        str+=f" {x} ways in front of you."
        print(str)
        return 0

    def dragonEvent(self):
        str=self.starStr
        str+="The last battle"
        print(str)
        return 0
    def spawnEvent(self,player):
        str=self.starStr
        str+=f"Welcome,{player.name}. Now you're at the spawn plot."
        print(str)
        return 0

    def Attack(self,attacker,attacked):#returns the damage caused by the attack
        d2=attacked.defense
        a1=attacker.attack
        damage=0
        # if attack is bigger than defense,then damage= atk-def
        #if attack is smaller than defense,then damage= 1
        if a1>d2:
            damage+=(a1-d2)
        else:
            damage+=1

        return damage

    def battle(self,player,monster):
        str=self.starStr
        str+=f"An enemy '{monster.name}' appears. Lv:{monster.level} Attack:{monster.attack} Defense:{monster.defense}\nYou faught against the enemy.\n And this is the result."
        print(str)
        time.sleep(1)
        d1=self.Attack(player,monster)
        d2=self.Attack(monster,player)
        win=True
        while(True):
            if(player.level>=monster.level):
                monster.health-=d1
                if(monster.health<=0):
                    print(f"You win. You beat the {monster.name}")
                    time.sleep(1)
                    print(f"Bonus:Money from your enemy:{monster.money}")
                    player.money += monster.money
                    break
                player.health-=d2
                if(player.health<=0):
                    print(f"You lose.You were killed the {monster.name}")
                    win=False
                    break
            else:
                player.health -= d2
                if(player.health<=0):
                    print(f"You lose.You were killed the {monster.name}")
                    win=False
                    break
                monster.health -= d1
                if (monster.health <= 0):
                    print(f"You win. You beat the {monster.name}")
                    time.sleep(1)
                    print(f"Bonus:Money from your enemy:{monster.money}")
                    player.money+=monster.money
                    break
        self.printStatus(player)
        return win
    def couldAfford(self,player,price):
        if(player.money<price):
            print(self.starStr)
            time.sleep(1)
            print("Inefficient money!")
            return False
        else:
            player.money-=price
            return True
    def purchase(self,player,type):
        if(type == 1):
            self.printStatus(player)
            while (True):
                print(open('event/eventMerchant.txt').read())
                enter = input()
                if (enter == '1'):
                    if (self.couldAfford(player, 100) == True):
                        self.restore(player, 50)
                elif (enter == '2'):
                    if (self.couldAfford(player, 100) == True):
                        player.attack += 10
                elif (enter == '3'):
                    if (self.couldAfford(player, 50) == True):
                        player.defense += 5
                elif (enter == '4'):
                    if (self.couldAfford(player, 100) == True):
                        player.level += 1
                        player.maxHealth += 100
                        player.health += 100
                elif (enter == '5'):
                    break
                else:
                    print("Invalid Input!")
                self.printStatus(player)
        if(type == 2):
            self.printStatus(player)
            while (True):
                print(open('event/eventMerchant2.txt').read())
                enter = input()
                if (enter == '1'):
                    if (self.couldAfford(player, 150) == True):
                        self.restore(player, 150)
                elif (enter == '2'):
                    if (self.couldAfford(player, 125) == True):
                        player.attack += 25
                elif (enter == '3'):
                    if (self.couldAfford(player, 75) == True):
                        player.defense += 10
                elif (enter == '4'):
                    if (self.couldAfford(player, 180) == True):
                        player.level += 1
                        player.maxHealth += 200
                        player.health += 200
                elif (enter == '5'):
                    break
                else:
                    print("Invalid Input!")
                self.printStatus(player)
        if(type == 3):
            self.printStatus(player)
            while (True):
                print(open('event/eventMerchant3.txt').read())
                enter = input()
                if (enter == '1'):
                    if (self.couldAfford(player, 200) == True):
                        self.restore(player, 300)
                elif (enter == '2'):
                    if (self.couldAfford(player, 150) == True):
                        player.attack += 50
                elif (enter == '3'):
                    if (self.couldAfford(player, 100) == True):
                        player.defense += 20
                elif (enter == '4'):
                    if (self.couldAfford(player, 250) == True):
                        player.level += 1
                        player.maxHealth += 300
                        player.health += 300
                elif (enter == '5'):
                    break
                else:
                    print("Invalid Input!")
                self.printStatus(player)

    def restore(self,player,amount):
        if(player.health+amount > player.maxHealth):
            player.health=player.maxHealth
        else:
            player.health+=amount
        return 0
    def win(self):
        print("Congratulations, you win.\nQuit game? (y/n)")
        quit = False
        i = 0
        while (i == 0):
            enter = input()
            if (enter.lower() == 'y'):
                quit = True
                i = 1
            elif (enter.lower() == 'n'):
                print("You choose to start from the beginning.")
                i = 1
            else:
                print("Invalid Input")
        if (quit == True):
            routeFlag= '-2'
        else:
            routeFlag = '-1'
        return routeFlag
    def bombBoxEvent(self,player):
        flag = True
        i = 0
        while (i == 0):
            print(open('event/eventBox.txt').read())
            enter = input()
            if (enter.lower() == 'y'):
                player.suicide()
                str = self.starStr
                str += "Oops you opened a box with a bomb inside. You died."
                print(str)
                flag = False
                i = 1
            elif (enter.lower() == 'n'):
                print("You choose not to open the box.")
                i = 1
            else:
                print("Invalid Input")
        self.printStatus(player)
        return flag
    def camping(self,player):
        print(open('event/eventCampfire.txt').read())
        while (True):
            enter = input()
            if (enter.lower() == 'y'):
                print("Health restored after a night's sleeping.")
                self.restore(player, player.maxHealth)
                break
            elif (enter.lower() == 'n'):
                print("You choose not to make a campfire.")
                break
            else:
                print("Invalid Input")
        self.printStatus(player)

    def eatFruits(self,player,type):#type 1=attack 2=defense 3=poison
        print(open('event/eventTree.txt').read())
        i=0
        if type==1:
            while (i == 0):
                enter = input()
                if (enter.lower() == 'y'):
                    print("Ah! Delicious fruit. Taste like plum. Attack +10.")
                    player.attack += 10
                    i = 1
                elif (enter.lower() == 'n'):
                    print("You choose not to taste strange fruits.")
                    i = 1
                else:
                    print("Invalid Input")
        elif type==2:
            while (i==0):
                enter = input("Your Decision:")
                if (enter.lower() == 'y'):
                    print("Ah! Delicious fruit. Taste like cherry. Defense+10.")
                    player.defense += 10
                    i=1
                elif (enter.lower() == 'n'):
                    print("You choose not to taste strange fruits.")
                    i=1
                else:
                    print("Invalid Input")
        else:
            while (i==0):
                enter = input("Your Decision:")
                if (enter.lower() == 'y'):
                    print("After tasting the fruit, your had a stomachache.\n It seemed to be poisonous. Health-100.")
                    player.health-=100
                    i=1
                elif (enter.lower() == 'n'):
                    print("You choose not to taste strange fruits.")
                    i=1
                else:
                    print("Invalid Input")
        self.printStatus(player)

    def goldBox(self,player,type):
        self.printStatus(player)
        print(open('event/eventBox.txt').read())
        flag=True
        if type==1:
            while (flag == True):
                enter = input()
                if (enter.lower() == 'y'):
                    print("A full box of gold coins. A good day.")
                    player.money += 50
                    flag = False
                elif (enter.lower() == 'n'):
                    print("You choose not to open the box.")
                    flag = False
                else:
                    print("Invalid Input")
        elif type==2:
            while (flag == True):
                enter = input()
                if (enter.lower() == 'y'):
                    print("A full box of gold coins. A good day.")
                    player.money += 500
                    flag = False
                elif (enter.lower() == 'n'):
                    print("You choose not to open the box.")
                    flag = False
                else:
                    print("Invalid Input")
        self.printStatus(player)