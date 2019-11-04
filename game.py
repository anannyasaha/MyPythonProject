# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:22:33 2018

@author: Anannya
"""

class character:
    def __init__(self,name, hp, attack, defense, magic=0):
        self.name=name
        self.hp=hp
        self.maxhp=hp
        self.attackpower=attack
        self.defensepower=defense
        self.magic=magic
    def __str__(self):
        return self.name + " has "+str(self.hp) +" HP"
    
        
    def isDead(self):
        if self.hp<=0:
            return True
        else:
            return False
    
    def attack(self,otherCharacter):
        damage=self.attackpower-otherCharacter.defensepower
        
        otherCharacter.hp-=max(0,damage)
        otherCharacter.hp=max(0,otherCharacter.hp)
        
        
        return self.name+" does "+str(damage)+"points of damage to Boss"
    def heal(self,party):
        for i in party:
            
            self.hp+=self.magic
            
            return self.name+" heals "+str(self.magic)+" hp for "+i.name
def isPartyDead(party):
        ctr=0
        for i in party:
            result=i.isDead()
            if(result==True):
                ctr+=1
        if ctr==len(party):
            return True
        else:
            return False

krogg=character("krogg",180,20,20)   
glinda=character("Glinda",120,5,15,5)
geoffrey = character('Geoffrey', 150, 15, 15)
party = [krogg, glinda, geoffrey]
boss = character('Boss', 500, 25, 15)
round = 1
while (not boss.isDead()) and (not isPartyDead(party)):
    
    
    print('Round', round)
    
 # krogg attacks
    krogg.attack(boss)
    
    
 # geoffrey attacks
    geoffrey.attack(boss)

 # glinda heals
    glinda.heal(party)
 # boss attacks
    for partyMember in party:
        boss.attack(partyMember)
 # show progress
    for partyMember in party:
        print(partyMember)
        print(boss)
        print('')

        round += 1
    if isPartyDead(party):
    
        print('Your whole party is dead. You lose.')
    elif boss.isDead():
    
        print('The boss is dead. You are victorious!')