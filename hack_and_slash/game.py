import sys
from character import Character
from monster import Goblin
from monster import Troll
from monster import Dragon

class Game:
    
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon(),
        ]
        self.monster = self.get_monster()
        
    def get_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None
    
    def monster_turn(self):
        if self.monster.attack():
            print("{} is attacking".format(self.monster))
            if input('Dogde? Y/N :').lower() == 'y':
                if self.player.dodge():
                    print('You dodged the attack')
                else:
                    print("You could not dodge and {} hit you".format(self.monster))
                    self.player.hit_points -= 1
            else:
                print("{} hit you".format(self.monster))
                self.player.hit_points -= 1
        else:
            print('{} is not attacking this turn'.format(self.monster))

        
    def player_turn(self):
        player_choice = input('[A]ttack, [R]est, [Q]uit : ').lower()
        if player_choice == 'a':
            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodge your attack".format(self.monster))
                else:
                    print('Attack successful')
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
            else:
                print('Attack unsuccessful')
        elif player_choice == 'r':
            self.player.rest()
        elif player_choice == 'q':
            sys.exit()
        else:
            return self.player_turn()

        
    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += 1
            print('You killed {}'.format(self.monster))
            self.monster = self.get_monster()

    
    def __init__(self, **kwargs):
        self.setup()
        
        while self.player.hit_points and (self.monsters or self.monster):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn()
            print('-'*20)
            self.player_turn()
            self.cleanup()
            print('\n'+'='*20)
            
        if self.player.hit_points:
            print('YOU WIN !!!')
        elif self.monster or self.monsters:
            print('YOU LOSE !!!')
        sys.exit()

            
    