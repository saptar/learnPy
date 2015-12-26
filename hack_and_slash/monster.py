import random
from combat import Combat

COLORS = ['red', 'blue', 'green', 'yellow', 'grey']


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sowrd'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        return "{} {}; HP : {}; XP : {}".format(
                                                self.color,
                                                self.__class__.__name__,
                                                self.hit_points,
                                                self.experience
                                                )


    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    max_hit_points = 3
    max_experience = 5
    sound = 'squeak'
    
    
class Troll(Monster):
    max_hit_points = 7
    min_hit_points = 2
    max_experience = 6
    min_experience = 3
    sound = 'growl'
    
class Dragon(Monster):
    max_hit_points = 10
    min_hit_points = 5
    max_experience = 10
    min_experience = 5
    sound = 'raaaaaaar'
    
    