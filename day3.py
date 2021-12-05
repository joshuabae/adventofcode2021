# read txt file
import os 
print(os.getcwd())
with open('files/day3.txt') as f:
    data = f.read().splitlines() 
    binary_list = [num for num in data]

# print(binary_list[0:10])

from statistics import mode
from collections import defaultdict

### part1
def power_calc(binaries):
    hash_map = {}
    for i in range(0, 12):
        hash_map[i] = [num[i] for num in binaries]
    
    gamma = ''
    for key in hash_map:
        gamma += max(set(hash_map[key]), key=hash_map[key].count)
    
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

    gamma = int(gamma, 2) 
    epsilon = int(epsilon, 2)

    return gamma * epsilon

# print(power_calc(binary_list))


### part2
def oxygen_calc(binaries):
    oxy_bin = binaries.copy()
    co2_bin = binaries.copy()
    for i in range(0, 12):
        # get first bit for all numbers
        oxy_map = defaultdict(list)
        for bit in oxy_bin:
            if bit[i] == '0':
                oxy_map[0].append(bit)
            else:
                oxy_map[1].append(bit)
        if len(oxy_map[1]) >= len(oxy_map[0]):
            oxy_bin = oxy_map[1]
        else:
            oxy_bin = oxy_map[0]

        if len(oxy_bin) == 1:
            oxygen = int(oxy_bin[0], 2)
        
    for i in range(0, 12):
        co2_map = defaultdict(list)
        for bit in co2_bin:
            if bit[i] == '0':
                co2_map[0].append(bit)
            else:
                co2_map[1].append(bit)
        if len(co2_map[0]) <= len(co2_map[1]):
            co2_bin = co2_map[0]
        else:
            co2_bin = co2_map[1]

        if len(co2_bin) == 1:
            co2 = int(co2_bin[0], 2)

    return oxygen * co2
    


print(oxygen_calc(binary_list))
