''' @ author
Gianni M. Javier
'''

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

# * Customize the attack methods on both the Ninja and Pirate class.
    def attack ( self , ninja ):
        import random
        pirate_attack_speed = random.randint(0,self.speed)
        ninja_defense_speed = random.randint(0,ninja.speed)
        if pirate_attack_speed > ninja_defense_speed:
            ninja.health -= self.strength
            print(f'{self.name} attacked and damaged {ninja.name} by {self.strength}.')
        elif ninja_defense_speed > pirate_attack_speed :
            print(f'{ninja.name} dodged the attack from {self.name}.')
        else:
            print(f'{self.name} and {ninja.name} have an equal attack speed and defense speed, respectively.\nNeither opponent took damage.')
        return self

