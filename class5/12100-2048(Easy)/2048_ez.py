'''
https://www.acmicpc.net/problem/12100 - 2048 (Easy)

소요시간 X분, 풀이X, 유튜브 강의영상 시청 후 구현

아이디어 : 한 행에 대해서 왼쪽으로 움직이는 함수를 구현함.
           이 때 0으로만 구성된 새 배열을 만든 뒤 원본에서 0이 아닌 숫자가 나올 때까지 찾다가
           0이 아닌 숫자를 만나면 같은 숫자가 이미 들어있다면 *2를 한 뒤 인덱스변수를 올려주고
           다른 숫자라면 단순히 인덱스변수를 올려준 뒤 값을 넣음

           이 함수를 모든 행에 대해 실행하면 되는데, 다른 방향에 대한 방법은 판 자체를 돌려서 해결하면 됨
           즉, 아래 방향으로 움직여야 한다면 판을 90도 돌린 뒤 왼쪽으로 움직이는 것과 같으니
           배열을 90도씩 회전시키는 rotate 함수를 만들어 각 방향마다 회전시킨 뒤에 움직임

           최종적으로 4가지 방향을 5번씩 하는 4**5 만큼 반복문을 돌려 모든 경우의 수에 대해 검사하면
           최대값을 브루트포스로 찾을 수 있음

시간복잡도 : (20 * 20 * 5) * 4**5
              ^^^^^^^   ^    ^^^^
        기울임 처리  기울이는    ㄴ 가능한 방향의 개수
        연산 횟수    경우의 수

자료구조 : 

느낀점 : 처음 구현을 시도할 때는 버블소트와 유사한 방식으로 움직임을 구현하다가 한 번 합쳐진 숫자는
         더 이상 못 합쳐진다는 조건을 보고 포기하고 유튜브 강의영상을 시청했음

         체스 판 자체를 돌린다는 아이디어가 상당히 중요하다고 생각함
'''

import sys

def rotate():
    global rst

    new = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new[i][j] = rst[i][j]

    for i in range(N):
        for j in range(N):
            rst[i][j] = new[N-1-j][i]

def move(di):
    global rst

    for _ in range(di): rotate()

    for i in range(N):
        moved = [0 for _ in range(N)]
        idx = 0

        for j in range(N):
            if rst[i][j] == 0: continue
            
            if moved[idx] == 0: moved[idx] = rst[i][j]
            elif moved[idx] == rst[i][j]:
                moved[idx] *= 2
                idx += 1
            else:
                idx += 1
                moved[idx] = rst[i][j]
        
        for j in range(N):
            rst[i][j] = moved[j]

N = int(sys.stdin.readline())
matrix = list()
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

rst = [[0 for _ in range(N)] for _ in range(N)]
ans = 0
for temp in range(4**5):

    for i in range(N):
        for j in range(N):
            rst[i][j] = matrix[i][j]

    brute = temp
    for i in range(5):
        di = brute % 4
        brute = brute // 4
        move(di)
    
    for i in range(N):
        for j in range(N):
            ans = max(ans, rst[i][j])

print(ans)