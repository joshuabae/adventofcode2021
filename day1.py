### part1

# read txt file
import os 
print(os.getcwd())
with open('files/day1.txt') as f:
    data = f.read().splitlines() 
    num_list = [int(num) for num in data]

print(num_list[0:10])

def count_inc(depth_lst):
    count = 0 
    for j in range(1, len(depth_lst) - 1):
        if depth_lst[j] > depth_lst[j-1]:
            count += 1
    return count

result = count_inc(num_list)
print(result)

### part2
def slide_window(depth_lst):
    count = 0
    