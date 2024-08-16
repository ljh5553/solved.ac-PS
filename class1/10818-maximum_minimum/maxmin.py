length = input()
temp = input()
vals = temp.split()

max = -1000001
min = 1000001

for val in vals:
    if int(val) > max : max = int(val)
    if int(val) < min : min = int(val)

print(min, max)