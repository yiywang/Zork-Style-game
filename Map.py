class Map(object):
    def __init__(self):
        self.regions=[]
        self.setRegion()
    def setRegion(self):#Geographic Features of this game map
        for i in range(1,18):
            if i==1 or 4 or 11:
                self.regions.append('forest')
            elif i==2 or 12:
                self.regions.append('cave')
            elif i==3 or 13 or 15:
                self.regions.append('valley')
            elif i==5 or 7 or 10 or 14 or 17:
                self.regions.append('plain')
            elif i==8:
                self.regions.append('dragoncave')
            else:
                self.regions.append('highland')
    def switch(self,fromX,toY,toZ):
        str0='crossing/crossing'
        str1='_'
        str2='.txt'
        str3=str0+str(fromX)+str1+str(toY)+str1+str(toZ)+str2
        print(open(str3).read())
        while (True):
            enter = input()
            if (enter == '1'):
                routeFlag = str(toY)
                break
            elif (enter == '2'):
                routeFlag = str(toZ)
                break
            else:
                print("Invalid Input!")
        return routeFlag

    def location(self,route):
        print(f"Your location:Route {route}\nRegion:{self.regions[route-1]}")