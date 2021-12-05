# read txt file
import os 
print(os.getcwd())
with open('files/day4.txt') as f:
    data = f.read().splitlines()
    order = data.pop(0)

    boards = []
    for i in range(1, len(data)-1, 6):
        board = [[str(num) for num in line.split()] for line in data[i:i+5]]
        boards.append(board)


def tic_tac(numbers, game_boards):
    return None


    
