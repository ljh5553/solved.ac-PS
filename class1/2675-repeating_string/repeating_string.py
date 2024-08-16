num_testcase = input()

for i in range(int(num_testcase)):
    rst = ""
    str = input()
    data = str.split()
    for j in range(len(data[1])):
        rst += data[1][j] * int(data[0])
    print(rst)