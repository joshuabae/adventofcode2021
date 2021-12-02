### part1

# read txt file
import os 
print(os.getcwd())
with open('files/day1.txt') as f:
    data = f.read().splitlines() 
    num_list = [int(num) for num in data]

print(num_list[0:10])

### part1
def count_inc(depth_lst):
    count = 0 
    for i in range(1, len(depth_lst) - 1):
        if depth_lst[i] > depth_lst[i-1]:
            count += 1
    return count

print(count_inc(num_list))

### part2
def slide_window(depth_lst):
    count = 0
    for i in range(1, len(depth_lst) - 3):
        window2 = depth_lst[i] + depth_lst[i+1] + depth_lst[i+2]
        window1 = depth_lst[i-1] + depth_lst[i] + depth_lst[i]
        if window2 > window1:
            count += 1
    return count

print(slide_window(num_list))