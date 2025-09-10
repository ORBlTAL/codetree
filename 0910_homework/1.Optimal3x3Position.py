import sys
sys.stdin = open('input1.txt')
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]
max_val = 0
for i in range(N - 2):
    for j in range(N - 2):
        r , c = i+1, j+1
        cnt = arr[r][c]
        for k in range(8):
            nr, nc = r + dr[k] , c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1:
                    cnt +=1
        # print(cnt)
        if max_val < cnt:
            max_val = cnt
print(max_val)