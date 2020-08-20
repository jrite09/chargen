import math
import random

weapons = ["Battleaxe", 'Club', 'Flail', 'Greatsword', 'Halberd', 'Handaxe', 'Light Hammer', 'Longsword', 'Mace', 
'Maul', 'Morningstar', 'Quarterstaff', 'Spear', 'Shortsword', 'War Pick', 'Warhammer', 'Greataxe']
armor = ['Chain Mail', 'Leather Armor', 'Padded Armor', 'Studded Leather Armor', 'a Chain Shirt', 'Hide Armor', 'Scale Mail', 'Ring Mail']
races = ["human", "half elf", "dwarf", "elf", 'halfling', 'gnome', 'tiefling', 'dragonborn', 'half orc']
packs = ["Soldier's pack", "Medic's pack", "Soldier's pack", "Sapper's pack"]


# rolls a d6
def d6():
    output = random.randint(1, 6)
    return output

# returns the sum of X number of d6
def statRoll(dice):
    holder = []
    for _ in range(dice):
        holder.append(d6())
    holder.sort()
    holder.pop(0)
    output = sum(holder)
    return output

def ageRoll():
    output = random.randint(16, 45)
    return output

def gearRoll():
    equipWeapon = random.choice(weapons)
    equipArmor = random.choice(armor)
    equipPack = random.choice(packs)
    return [equipWeapon, equipArmor, equipPack]

# the character class. rolls stats, age, etc upon initialization
class Character:
    age = None
    race = None
    outGear = None
    outStats = None
    outputString = ""

    def __init__(self, race):
        self.race = race
        self.stats = []
        self.gear = []
        self.age = ageRoll()
        self.gear = gearRoll()

        #print("Testing race: {}".format(self.race))

        if (self.race == "human"):
            for _ in range(6):
                self.stats.append(statRoll(4) + 1)
        elif (self.race == "elf" or self.race == "halfling"):
            for _ in range(6):
                if (_ == 1):
                    self.stats.append(statRoll(4) + 2)
                else:
                    self.stats.append(statRoll(4))
        elif (self.race == "dragonborn"):
            for _ in range(6):
                if (_ == 0):
                    self.stats.append(statRoll(4) + 2)
                elif (_ == 5):
                    self.stats.append(statRoll(4) + 1)
                else:
                    self.stats.append(statRoll(4))
        elif (self.race == "gnome"):
            for _ in range(6):
                if (_ == 3):
                    self.stats.append(statRoll(4) + 2)
                else:
                    self.stats.append(statRoll(4))
        elif (self.race == "dwarf"):
            for _ in range(6):
                if (_ == 2):
                    self.stats.append(statRoll(4) + 2)
                else:
                    self.stats.append(statRoll(4))
        elif (self.race == "half elf"):
            # To do: implement random +1 to two stats
            for _ in range(6):
                if (_ == 5):
                    self.stats.append(statRoll(4) + 2)
                else:
                    self.stats.append(statRoll(4))
            for _ in range(2):
                num = d6() - 1
                self.stats[num] = self.stats[num] + 1
        elif (self.race == "half orc"):
            for _ in range(6):
                if (_ == 0):
                    self.stats.append(statRoll(4) + 2)
                elif (_ == 2):
                    self.stats.append(statRoll(4) + 1)
                else:
                    self.stats.append(statRoll(4))
        elif (self.race == "tiefling"):
            for _ in range(6):
                if (_ == 3):
                    self.stats.append(statRoll(4) + 1)
                elif (_ == 5):
                    self.stats.append(statRoll(4) + 2)
                else:
                    self.stats.append(statRoll(4))
        
    def reportChar(self):
        self.outputString = "Your character is a " + str(self.age) + " year old " + self.race + " soldier. His stats are:\nStrength: {}, Dexterity: {}, Constitution {}, Intelligence: {}, Wisdom: {}, Charisma {}.\nHe is wielding a {}, is clad in {}, and is carrying a {}.".format(self.stats[0], self.stats[1], self.stats[2], self.stats[3], self.stats[4], self.stats[5], self.gear[0], self.gear[1], self.gear[2])
        return self.outputString
        # print("His stats are:")
        # print("Strength: {}, Dexterity: {}, Constitution {}, Intelligence: {}, Wisdom: {}, Charisma {}.".format(self.stats[0], self.stats[1], self.stats[2], self.stats[3], self.stats[4], self.stats[5]))
        # print("He is wielding a {}, is clad in {}, and is carrying a {}.".format(self.gear[0], self.gear[1], self.gear[2]))
    
    def reportStats(self):
        self.outStats = "His stats are:\nStrength: {}, Dexterity: {}, Constitution {}, Intelligence: {}, Wisdom: {}, Charisma {}.".format(self.stats[0], self.stats[1], self.stats[2], self.stats[3], self.stats[4], self.stats[5])
        print(self.outStats)

    def reportGear(self):
        self.outGear = ", ".join(self.gear)
        return self.outGear

char = Character('human')
char.reportChar()
