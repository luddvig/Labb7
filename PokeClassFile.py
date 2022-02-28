

class Pokemon():
    # 13 attribut
    def __init__(self,number,name,type1,type2,total,hp,attack,defense,sp_attack,sp_defense,speed,generation,legendary):
        self.number = number
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.hp < other.hp

    def __gt__(self, other):
        return self.speed > other.speed

    def __add__(self, other):
        return int(self.attack) + int(other.attack)

    def __bool__(self):
        return self.legendary

    def __contains__(self, item):
        if item in self.number:
            return True
        else:
            return False

