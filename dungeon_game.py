#!/usr/bin/env python3

import random

# cells in the game
CELLS = [(0,0),(0,1),(1,2),
         (1,0),(1,1),(1,2),
         (2,0),(2,1),(2,2)
         ]

def draw_map(player):
    print(' _ _ _') # top of the map
    tile ='|{}' # template for the left or center colm
    for idx, cell in enumerate(CELLS):
        if idx in [0,1,3,4,6,7]:
            if cell == player:
                print(tile.format('X'),end='')
            else:
                print(tile.format('_'),end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))

def move_player(player,move):
    # player = (x,y)
    
    x,y = player
    
    if move == 'LEFT':
        y -= 1
    if move == 'RIGHT':
        y += 1
    if move == 'UP':
        x -= 1
    if move == 'DOWN':
        x += 1
    # get the players location
    # if the move is LEFT , y-1
    # if the move is RIGHT , y+1
    # if the move is UP , x-1
    # if the move is DOWN , x+1
    return x,y

def get_moves(player):
    moves = ['LEFT','RIGHT','UP','DOWN']
    # player = (x,y)
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')
    # if player's y is 0, remove LEFT
    # if player's x is 0, remove UP
    # if player's y is 2, remove RIGHT
    # if player's x is 2 , remove DOWN
    return moves
    
def get_locations():
    # random location for the monster
    # random location for the player
    # random location for the door

    monster = random.choice(CELLS)
    player  = random.choice(CELLS)
    door    = random.choice(CELLS)

    # if loc of player,monster or door are same , do it again
    if monster == door or player == monster or door == player:
        return get_locations()
    else:
        return player,monster,door
    # return the monster,door, player

print('Welcome to the dungeon!')

player, monster, door = get_locations()


while True:
    moves = get_moves(player)
    print('You are current in room {}'.format(player)) # add the co-ords of the room
    draw_map(player)
    print('You can move {}'.format(moves)) # fill in available moves
    print('Type QUIT to quit')
    
    move = input("Enter your move ")
    move = move.upper()
    if move == 'QUIT':
        break
    if move in moves:
        player = move_player(player,move)
    else:
        print('Cannot move; hit the wall')
        continue
    if player == door:
        print('Good job , you escaped !!!')
        break
    if player == monster:
        print('Monster has eaten you ; GAME OVER!!!')
        break
    
    
    # if the move is good, change the players current position
    # if the move is bad, don't change anything
    # if the player current position is that of the door, player wins
    # if the player current position is that of the monster,player looses.