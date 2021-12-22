# read txt file
import os 
print(os.getcwd())
with open('files/day4.txt') as f:
    data = f.read().splitlines()
    order = data.pop(0).split(',')

    boards = []
    for i in range(1, len(data)-1, 6):
        board = [[[str(num), 'False'] for num in line.split()] for line in data[i:i+5]]
        boards.append(board)

### part 1
def mark_rows(number, game_board):
    for row in game_board:
        for col in row:
            if col[0] == number:
                col[1] = 'True'
    return game_board

def check_row(game_board):
    for row in game_board:
        marked = [spot[1] for spot in row]
        if all(item == 'True' for item in marked):
            return True
        else:
            return False


def check_col(game_board):
    for i in range(0,5):
        marked_col = []
        for row in game_board:
            col = row[i][1]
            marked_col.append(col)
        if all(item == 'True' for item in marked_col):
            return True
        else:
            return False
    
def get_score(game_board, called_nums):
    score = 0
    for row in game_board:
        unmarked = [int(spot[0]) for spot in row if spot[1] == 'False']
        score += sum(unmarked)
        print(score)
    result = score * int(called_nums[-1])
    return(result)


def get_winner(game_boards, nums):
    called = []
    for num in nums:
        print(num)
        called.append(num)
        for board in game_boards:
            board = mark_rows(num, board)
            if len(called) >= 5:
                if check_row(board) or check_col(board):
                    print(board)
                    return(get_score(board, called))


print(get_winner(boards, order))



### part 2














# print(order.split(','))

# print(mark_rows('48', boards[1]))
# print(mark_rows('13', boards[1]))
# print(mark_rows('84', boards[1]))
# print(mark_rows('16', boards[1]))
# print(mark_rows('99', boards[1]))
# num_lst = [9]
# print(get_score(boards[1], num_lst))

# print(mark_rows('48', boards[1]))
# print(mark_rows('71', boards[1]))
# print(mark_rows('59', boards[1]))
# print(mark_rows('45', boards[1]))
# print(mark_rows('63', boards[1]))
# print(check_row(boards[1]))