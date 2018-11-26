#formulae#
    #TESTED:
    #expGainFromFight = (myPet.LVL * opponentPet.LVL) / 7 * participants
        #participants = how many pets were used before opponent faints
    #maxEXP = LVL**3/12.5
        #12.5 = growth rate

opponentLVL = 30
EXPgrowthRate = 12.5

class Pet():
    def __init__(self):
        global opponentLVL
        self.indexNum = 1
        self.name = "DUCK" #Turn into a text file search w/ indexNum
        self.HP = 100
        self.maxHP = 100
        self.LVL = 30
        self.EXP = 0
        self.maxEXP = (100 + self.LVL**3)/EXPgrowthRate
        print(self.maxEXP)
        
