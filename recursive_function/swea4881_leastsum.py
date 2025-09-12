"""
가야하는 곳의 위치 순회는 구현함
근데 그 좌표의 값들의 합을 N 번만큼만 누적하고, 최소를 비교해야 하는데....
"""
# import sys
# sys.stdin = open('input2.txt')
#
#
# def calc(depth , N, k):
#     min_val = float('inf')
#     if depth == N:
#         return k
#
#     for i in range(N):
#         if not state[i]:
#             state[i] = True
#             val = calc(depth + 1, N, k + arr[depth][i])
#             min_val = min(min_val, val)
#             state[i] = False
#     return min_val
#
# T = int(input())
# for tc in range(1, 1 + T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     state = [False] * N
#     result = calc(0,N, 0)
#     print(result)



import sys
sys.stdin = open('input2.txt')


def calc(depth, N, k):
    global min_val # 글로벌로 호출

    # 가지치기, 누적합인 k가 min_val 보다 크면 이미 최소가 아니므로 그때의 경우를 종료
    if k >= min_val:
        return
    # 깊이가 N 이 되면 다 도달한 것이므로 이때의 최소합을 구하고 종료
    if depth == N:
        min_val = min(min_val, k)
        return
    # depth로 행, i로 열을 탐색, 한행에 한 열씩 , 그리고 state[i]의 논리 처리를 통해서 같은열 안고르게 처리
    for i in range(N):
        if not state[i]:
            state[i] = True
            calc(depth + 1, N, k + arr[depth][i]) # k에 고른 좌표의 값을 넣어줘서 누적을 구해줌
            state[i] = False # 재귀가 끝나고 돌아오면 False를 해줘서 해당 열을 방문 가능토록 바꾸어줌

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    state = [False] * N # 동일한 열을 방문하지 않도록 하기위한 상태 state 리스트
    min_val = float('inf')
    calc(0, N, 0) # 함수호출
    print(f'#{tc}',min_val)