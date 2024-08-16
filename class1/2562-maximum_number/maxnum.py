nums = []
max = 0
max_idx = -1

for i in range(9):
    input_num = input()
    nums.append(int(input_num))
    
for idx, num in enumerate(nums):
    if num > max:
        max = num
        max_idx = idx
    
print(max)
print(max_idx + 1)