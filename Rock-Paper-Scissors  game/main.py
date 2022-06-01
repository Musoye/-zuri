import random


# the function to define the game
def game(player, computer):
    if (computer == 'R' and player =='S') or (computer == 'P' and player =='R') or (computer == 'S' and player =='P'):
        print("The computer user win")
    elif (player == 'R' and computer == 'S') or (player == 'P' and computer == 'R') or (player == 'S' and computer == 'P'):
        print("The player win")
    else:
        print("There is a tie")
        #if the computer and the player input is the same.The function go on recursively to satisfy the game.
        list =['R','P','S']
        player = input('Enter a letter between R,P,and S: ')
        player = player.upper()
        while player not in list:
            print("Error! Pick between the list")
            player = input('Enter a letter between R,P,and S: ')
            player = player.upper()   
        computer = random.choice(list)
        #what the player and the computer output
        dic = {'R':'Rock','P':'Paper','S':'Scissors'}
        output = f'Player { dic[player] } : Computer { dic[computer] }'
        print(output)
        #calling of function of the game
        game(player,computer)


list =['R','P','S']
player = input('Enter a letter between R,P,and S: ')
player = player.upper()
while player not in list:
    print("Error! Pick between the list")
    player = input('Enter a letter between R,P,and S: ')
    player = player.upper()
computer = random.choice(list)
#what the player and the computer output
dic = {'R':'Rock','P':'Paper','S':'Scissors'}
output = f'Player { dic[player] } : Computer { dic[computer] }'
print(output)
#calling of the game function
game(player,computer)