'''
아이디어 : 재귀적으로 트리 탐색. preorder -> root-l-r, inorder -> l-root-r, postorder -> l-r-root

시간복잡도 : ?

자료구조 : 트리를 표현하는 딕셔너리, 딕셔너리는 리스트를 가지고 있고 0번인덱스는 왼쪽자식 1번인덱스는 오른쪽자식
'''

import sys

def preorder(node):
    global ans

    ans += node
    if tree[node][0] != ".": preorder(tree[node][0])
    if tree[node][1] != ".": preorder(tree[node][1])
    return

def inorder(node):
    global ans

    if tree[node][0] != ".": inorder(tree[node][0])
    ans += node
    if tree[node][1] != ".": inorder(tree[node][1])
    return

def postorder(node):
    global ans

    if tree[node][0] != ".": postorder(tree[node][0])
    if tree[node][1] != ".": postorder(tree[node][1])
    ans += node
    return

N = int(sys.stdin.readline())
tree = dict()
for _ in range(N):
    inputnode, inputleft, inputright = map(str, sys.stdin.readline().split())
    tree[inputnode] = [inputleft, inputright]

ans = ""
preorder("A")
print(ans)
ans = ""
inorder("A")
print(ans)
ans = ""
postorder("A")
print(ans)