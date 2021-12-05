# read txt file
import os 
print(os.getcwd())
with open('files/day2.txt') as f:
    data = f.read().splitlines() 
    num_list = [num for num in data]

# print(num_list[0:10])

### part1
def calc_position(depth_list):
    hor = 0
    ver = 0
    for move in depth_list:
        split_move = move.split()
        direction = split_move[0]
        value = int(split_move[1])

        if direction == 'forward':
            hor += value
        elif direction == 'down':
            ver += value
        elif direction == 'up':
            ver -= value
    return hor * ver

# print(calc_position(num_list))


def calc_pos_aim(depth_list):
    hor = 0
    ver = 0
    aim = 0
    for move in depth_list:
        split_move = move.split()
        direction = split_move[0]
        value = int(split_move[1])
        if direction == 'forward':
            hor += value
            ver += aim * value
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
    return hor * ver


### part2
print(calc_pos_aim(num_list))