# read txt file
import os 
print(os.getcwd())
with open('files/day4.txt') as f:
    data = f.read().splitlines()
    order = data.pop(0)

    boards = []
    for i in range(1, len(data)-1, 6):
        board = [[[str(num), False] for num in line.split()] for line in data[i:i+5]]
        boards.append(board)

print(boards[1])

def mark_rows(number, game_board):
    for row in game_board:
        for col in row:
            if col[0] == number:
                col[1] = True
    return game_board

def check_row(game_board):
    for 


def check_col(game_board):
    


print(mark_rows('48', boards[1]))