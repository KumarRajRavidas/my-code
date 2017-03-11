'''class Animal:
    
    hungary = "yes"
    name="no name"
    owner="no Owner"
    
    def __init__(self):
        pass
    def set_owner(self, newOwner):
        self.owner = newOwner
        return
    def get_owner(self):
        return self.owner
    def noice(self):
        print('errrrrrrr')
        return
    
def main():
    dog = Animal() #object

    dog.set_owner('sue')  #i passed sue in the set_owner function
    print dog.get_owner()
    print dog.owner
    dog.noice()

if __name__ == '__main__':main() 
####################################################################
class Animal:
    
    
    hungary ="Yes"
    __furry = "Yes"
    __name = "No Name"
    __owner = "No Owner"

    def __init__(self): # The constructor function called when object is created
        name = "No Name"
        owner = "No Owner"
# There is a function called a destructor __del__, but its best to avoid it
    def set_owner(self, newOwner): # Accessor Method
        self.__owner = newOwner
        return

    def get_owner(self):
        return self.__owner

    def set_name(self, newName): # Accessor Method
        self.__name = newName
        return

    def get_name(self):
        return self.__name

    def noise(self): # self is a reference to the object
        print 'errr' # You use self so you can access attributes of the object
        return

    def move(self):
        print 'The animal moves forward'      # print Animal.__hiddenMethod(self) A Private method
        return

    def eat(self):
        print 'Crunch, crunch'
        return

    def furr(self):
        print self.__furry

def main():
    dog = Animal()
    dog.set_owner('Sue')
    dog.set_name('Jake')

    print dog.get_owner()
    print dog.get_name()

    if dog.hungary:
        dog.eat()
    else:
        dog.move()

    dog.noise()
    dog.furr()

if __name__ == '__main__': main()

#################################################################

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5



print(Point(7, 6).distanceFromOrigin())



def distanceFromOrigin(x,y):
        return ((x ** 2) + (y ** 2)) ** 0.5
    
print(distanceFromOrigin(7,8))
print(distanceFromOrigin(5,5))
print(distanceFromOrigin(2,6))
from raj.bisection import height
  
#Real world object : Atttributes & Capabilites
#Dog Attributes(Fields): Height , Weight, Favorite Food
#Dog Capabilities(Method/Function): Run ,Walk, Eat


class Dog:
    # self allows an object to refer to itself
    # It is like how you refer to yourself with my
    # We will take the values passed in and assign
    # them to the new Dog objects fields (attributes)
    def __init__(self , name="" , height=0, weight=0):
        self.name=name
        self.height=height
        self.weight=weight
        
    def run(self):
        print "{} the dog run" .format(self.name)
        
    def eat(self):
        print "{} the dog eats" .format(self.name)
        
    def bark(self):
        print "{} the dog barks" .format(self.name)
        
def main():
    #creat a new Dog objevt
    spot = Dog("Spot" ,66, 26)
    spot.bark()
    bowser =Dog()   
main()
from __main__ import name


#######################################################################
# Getters and Setters are used to protect our objects
# from assigning bad fields or for providing improved
# output


class Square:
    def __init__(self, height="0" , width="0"):
        self.height = height
        self.width = width
        
    #This is the getter
    @property
    def height(self):
        print "Reverting the height"
        return self.__height #this is private filde
    
    @height.setter
    def height(self, value):
        #we protect the height form receiving a bad value      
        if value.isdigit():
            self.__height=value
        else:
            print "Plese enter number foe height"
        
    @property
    def width(self):
        print "Reverting the height"
        return self.__width
            
    @width.setter
    def width(self, value):
        #we protect the height form receiving a bad value      
        if value.isdigit():
            self.__height=value
        else:
            print "Plese enter number foe height"
        
    
    def getArea(self): 
        return int(self.__width) * int(self.__height) #private attributes

def main():
    aSquare = Square()
    
    height = input("Enter height :")
    width = input("Enter width :")
    
    aSquare.height =height
    aSquare.width= width
    print "Height: ",aSquare.height
    print "width: ",aSquare.width
    print "The Area is :" , aSquare.getArea()

if __name__ == '__main__': main()'''
          
##################################################################

# ---------- WARRIORS BATTLE ----------
# We will create a game with this sample output
'''
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious
Game Over
'''
    
# Warrior & Battle class
import random
import math
#Warrior will have name ,health, and attack and block
#They  will have the capabilities to attack and block random amounts
class Warrior:
    def __init__(self,name="warrior" ,health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health= health
        self.attkMax= attkMax
        self.blockMax= blockMax
        
    def attack(self):
        #Random calculate the attack amount
        #random() return a value from 0.0 to 1.0
        attkAmt = self.attkMax  * (random.random() + .5)
        return attkAmt
    
    def block(self):
        #Random find how much helth was block
        blockAmt= self.blockMax * (random.random() + .5)
        return blockAmt
# The Battle class will have the capability to loop until 1 Warrior dies
# The Warriors will each get a turn to attack each turn

class Battle:
    def statrFight(self, warrior1, warrior2):
        
        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        
        while True:
            if self.getAttackResult(self, warrior1, warrior2 ) =="Game Over  ":
                print "Game Over"
                break
            if self.getAttackResult(self, warrior2, warrior1 ) =="Game Over  ":
                print "Game Over"
                break
    # A function will receive each Warrior that will attack the other
    # Have the attack and block amounts be integers to make the results clean
    # Output the results of the fight as it goes
    # If a Warrior dies return that result to end the looping in the
    # above function
 
    # Make this method static because we don't need to use self
    
    
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
        
        warriorBBlockAmt = warriorB.block()
        
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB
        
        print "{] attacks {} adn deals {} damage " .format(warriorA.name, warriorB.name, damage2WarriorB)
        
        
        print "{} is down to health ".format(warriorB.name,warriorB.health)
        
        if warriorB.health <=0:
            print "{} has died and {} is victory " .format(warriorB.name,warriorA.name)
            
            return "Game Over"
        else:
            return "Fight Again"
        
def main():
    #create 2 warrior:
    paul = Warrior("paul", 50,20,10)
    sam = Warrior("sam",50,20,10)
    #create Battle Object
    battle =Battle()
    #instance Battle
    battle.statrFight(paul, sam)
if __name__ == '__main__': main()
main()
    
    
    
        
           


    
        
    
    
    

   
            
        
    
        
        


        
















































