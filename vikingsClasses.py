import random
# Soldier


class Soldier:
    
    def __init__(self, health=0, strength=0):
        self.health=health
        self.strength=strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health=  self.health- damage
        return
    

# Viking


class Viking(Soldier):
    
    def __init__(self, name=0, health=0, strength=0):
        Soldier.__init__(self, health, strength)
        self.name=name
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health=  self.health - damage
        if self.health > 0: 
            return(f'{self.name} has received {damage} points of damage')
        if self.health <= 0: 
            return(f'{self.name} has died in act of combat')
        return
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health=0, strength=0):
        Soldier.__init__(self, health, strength)
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health=  self.health - damage
        if self.health > 0: 
            return(f"A Saxon has received {damage} points of damage")
        if self.health <= 0: 
            return(f'A Saxon has died in combat')
        
    
        
# War


class War:
    
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, one_viking):
        self.vikingArmy.append(one_viking)
        return
    
    def addSaxon(self, one_saxon):
        self.saxonArmy.append(one_saxon)
        return
    
    def vikingAttack(self):
        
        my_viking=random.choice(self.vikingArmy)  
        my_saxon=random.choice(self.saxonArmy) 
        
        result=my_saxon.receiveDamage(my_viking.attack())
        
        if my_saxon.health <= 0: 
            self.saxonArmy.remove(my_saxon)
        return result
    
    def saxonAttack(self):
        
        My_viking=random.choice(self.vikingArmy)  
        My_saxon=random.choice(self.saxonArmy) 
        
        result=My_viking.receiveDamage(My_saxon.attack())
        
        if My_viking.health <= 0:
            self.vikingArmy.remove(My_viking)
        return result
    
    def showStatus(self):
        lista_vacia=[]
        if self.vikingArmy == lista_vacia:
            return "Saxons have fought for their lives and survive another day..."
        elif self.saxonArmy == lista_vacia:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."
       