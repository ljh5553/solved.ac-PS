import sys

L = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

al = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
num = [i for i in range(1, 27)]

hash = 0
for i in range(L):
    al_idx = al.index(S[i])
    hash += (num[al_idx] * (31 ** i))

print(hash % 1234567891)