''' @ author
Gianni M. Javier
'''

class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

# * Customize the attack methods on both the Ninja and Pirate class.
    def attack( self , pirate ):
        import random
        ninja_attack_speed = random.randint(0,self.speed)
        pirate_defense_speed = random.randint(0,pirate.speed)
        if ninja_attack_speed > pirate_defense_speed :
            pirate.health -= self.strength
            print(f'{self.name} attacked and damaged {pirate.name} by {self.strength}.')
        elif pirate_defense_speed > ninja_attack_speed:
            print(f'{pirate.name} dodged the attack from {self.name}.')
        else:
            print(f'{self.name} and {pirate.name} have an equal attack speed and defense speed, respectively.\nNeither opponent took damage.')
        return self