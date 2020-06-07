import random

player_choose = ['Paper', 'Scissor', 'Rock']
opponent_choose = ['Paper', 'Scissor', 'Rock']

finally_player_choose = True
finally_opponent_choose = True
not_how_work = True

# Game rules function
def game_rules():
    print('stone paper scissor is a very old game whic is born a lor of time ago, in China.\n\n The game id in duo. You have to defeat your opponent by choosing the right object.\n\n In stone paper scissor there are 3 objects: Paper, Scissor and stone.\n\n The stone, beat the scissor, but it is beated by the paper.\n\n The paper, beat the stone, but it is beated by the scissor.\n\n Finally, the scissor beat the paper, but it is beated by the stone.\n\n Choose the right one to beat your opponet. Good luck. ')
    finally_ready = input('Are you now ready? (Y or N?) ')
    if finally_ready == 'Y':
        game(name, opponent_choose, finally_player_choose, finally_opponent_choose)
    else:
        print('Here we see the next time,', name)

# Game Initial function
def game_initial(not_how_work):
    print('So, Here we are. I Think you should now how the game works.')
    not_how_work = input("If you don't know how it works, simply type IDK, also if you know, type IK. ")
    # Player decision - 1
    if not_how_work == 'IDK':
        game_rules()
    else:
        game(name, opponent_choose, finally_player_choose, finally_opponent_choose)

#Game Function
def game(name, opponent_choose, finally_player_choose, finally_opponent_choose):
    finally_player_choose = input('What do you want to choose?\n1: Paper\n2: Scissor\n3: Stone\n')
    finally_opponent_choose = random.choice(opponent_choose)
    print(f'Your choice: {finally_player_choose}')
    print(f'The opponent choice: {finally_opponent_choose}')
    if finally_player_choose == '1' and finally_opponent_choose == opponent_choose[0]:
        print('Incredible, there is tie. Nice work,', name)
    elif finally_player_choose == '1' and finally_opponent_choose == opponent_choose[1]:
        print('You Lose! The opponent won.')
    elif finally_player_choose == '1' and finally_opponent_choose == opponent_choose[2]:
        print('You Won! Excellent,', name)
    elif finally_player_choose == '2' and finally_opponent_choose == opponent_choose[0]:
        print('You Won! Excellent,', name)
    elif finally_player_choose == '2' and finally_opponent_choose == opponent_choose[1]:
        print('Incredible, there is a tie!')
    elif finally_player_choose == '2' and finally_opponent_choose == opponent_choose[2]:
        print('You lose| The opponent won.')
    elif finally_player_choose == '3' and finally_opponent_choose == opponent_choose[0]:
        print('You lose! The opponent won.')
    elif finally_player_choose == '3' and finally_opponent_choose == opponent_choose[1]:
        print('You won! Excellent,', name)
    elif finally_player_choose == '3' and finally_opponent_choose == opponent_choose[2]:
        print('Incredible, there is a tie!')
    

# Players name
print('Welcome to stone paper scissor! My name is Matteo, and i will be your assistant during tha game.')
name = input("So, What's your name? ")
print('Oh Oh, Hello', name)

# If player want or not to play
play_or_not = input('So, do you want to play the game? (Y or N) ')

if play_or_not == 'Y':
    game_initial(not_how_work)
else:
    print('Here we see the next time,', name)
