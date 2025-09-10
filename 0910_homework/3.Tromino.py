# import sys
# sys.stdin = open('input3.txt')
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# # 상우하좌 순       좌상 우하 우상 좌하
# dr = [-1, 0, 1, 0, -1, 1, -1, 1]
# dc = [0, 1, 0, -1, -1, 1, 1, -1]
# """
# 발생할 수 있는 모든 경우는 다음과 같다.
# 1: ㄴ자블럭 에서
# 상우 상좌 하우 하좌 상우좌 하우좌
# 2: -자 블럭에서
# 좌우 상하 좌상우하 우상좌하
# """
# types= {
#     1: [1, 1, 0, 0, 0, 0, 0, 0],
#     2: [1, 0, 0, 1, 0, 0, 0, 0],
#     3: [0, 1, 1, 0, 0, 0, 0, 0],
#     4: [0, 0, 1, 1, 0, 0, 0, 0],
#     5: [1, 1, 0, 1, 0, 0, 0, 0],
#     6: [0, 1, 1, 1, 0, 0, 0, 0],
#     7: [0, 1, 0, 1, 0, 0, 0, 0],
#     8: [1, 0, 1, 0, 0, 0, 0, 0],
#     9: [0, 0, 0, 0, 1, 1, 0, 0],
#     10: [0, 0, 0, 0, 0, 0, 1, 1]
# }
#
# max_sum = 0
#
# for i in range(N):
#     for j in range(M):
#         for t in range(1, 11):   # 블록 10종류 순회
#             mask = types[t]
#             total = arr[i][j]    # 블록 시작점 값 포함
#             ok = True
#             for d in range(8):
#                 if mask[d] == 1:
#                     nr, nc = i + dr[d], j + dc[d]
#                     if 0 <= nr < N and 0 <= nc < M:
#                         total += arr[nr][nc]
#                     else:
#                         ok = False
#                         break
#             if ok:
#                 max_sum = max(max_sum, total)
#
# print(max_sum)

import sys
sys.stdin = open('input3.txt')
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방향 델타: 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [ 0, 1, 0,-1]

# 블록 타입 (중심 포함 총 3칸)
# ㄴ자 4가지 + 일자 2가지 = 총 6가지
types = {
    1: [1, 1, 0, 0],  # ㄴ자: 상 + 우
    2: [1, 0, 0, 1],  # ㄴ자: 상 + 좌
    3: [0, 1, 1, 0],  # ㄴ자: 우 + 하
    4: [0, 0, 1, 1],  # ㄴ자: 하 + 좌
    5: [0, 1, 0, 1],  # 일자: 좌 + 우
    6: [1, 0, 1, 0],  # 일자: 상 + 하
}

max_sum = 0

for i in range(N):
    for j in range(M):
        for t in range(1, 7):   # 블록 타입 6개 전부 시도
            mask = types[t]
            total = arr[i][j]   # 중심 포함
            ok = True
            for d in range(4):  # 상우하좌만 탐색
                if mask[d] == 1:
                    nr, nc = i + dr[d], j + dc[d]
                    if 0 <= nr < N and 0 <= nc < M:
                        total += arr[nr][nc]
                    else:
                        ok = False
                        break
            if ok:
                if total > max_sum:
                    max_sum = total

print(max_sum)