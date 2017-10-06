class car():
    no_of_wheels = 4
    def __init__(self,color,make,year):
        self.color = color
        self.make = make
        self.year = year

    def drive(self,acceleration):
        print("you can't drive this car yet")
    
    mycar.no_of wheels =12
    mysecondcar.no_of_wheeels=24

mycar = car("white","toyota","2012")
mysecondcar = car("green","voho","1976")

print(mysecondcar.drive(0))
