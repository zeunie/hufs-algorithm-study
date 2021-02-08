#pypy3 메모리초과
#python3 맞았습니다.
import sys

sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())  # 노드의 갯수
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)

# 부모저장
parents = [0 for _ in range(N + 1)]


def DFS(start, tree, parents):
    for i in tree[start]:  # 연결된 노드 모두탐색
        if parents[i] == 0:  # 한번도 방문한적이 없다면
            parents[i] = start  # 부모노드 저장
            DFS(i, tree, parents)


DFS(1, tree, parents)

for i in range(2, N + 1):
    print(parents[i])