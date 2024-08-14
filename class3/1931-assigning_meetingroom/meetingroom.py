import sys

N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

meetings.sort(key=lambda x: (x[0], x[1]))

rst = []
for meeting in meetings:
    if not rst:
        rst.append(meeting)
    elif rst[-1][1] > meeting[1]:
        rst[-1] = meeting
    elif rst[-1][1] <= meeting[0]:
        rst.append(meeting)

print(len(rst))