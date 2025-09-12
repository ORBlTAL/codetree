"""
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
"""

# def cross2(list_cross):
#     global cross2_1
#     cross2_1 += list_cross
#
# def cross1(list_cross):
#     global cross1_1
#     cross1_1 += list_cross
#
# # def col():
# #     pass
#
# def row(list_row):
#     global max_val
#     k = 0
#     for i in range(100):
#         k +=list_row[i]
#     if max_val < k:
#         max_val = k
#
# def arc(dept , arr, new_arr):
#     if dept == 100:
#         return
#     row(arr[dept])
#     row(new_arr[dept])
#     cross1(arr[dept][dept])
#     cross2(arr[dept][99-dept])
#     arc(dept +1, arr, new_arr)
#
# import sys
# sys.stdin = open('input.txt')
# T = 10
# for tc in range(1, 1+T):
#     _ = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     new_arr = list(map(list, zip(*arr)))
#     max_val = 0
#     cross1_1 = 0
#     cross2_1 = 0
#     arc(0,arr, new_arr)
#     print(f'#{tc}',max(max_val, cross1_1, cross2_1))

import sys
sys.stdin = open('input.txt')

def arc(idx, arr, n, max_row=0, max_col=0, cross1=0, cross2=0):
    if idx == n:  # 종료 조건
        return max(max_row, max_col, cross1, cross2)

    # 현재 행 합
    row_sum = sum(arr[idx])
    # 현재 열 합 (zip으로 미리 전치하지 않고 바로 계산)
    col_sum = sum(arr[i][idx] for i in range(n))

    # 대각선 합
    cross1 += arr[idx][idx]          # 좌상 → 우하
    cross2 += arr[idx][n - 1 - idx]  # 우상 → 좌하

    # 행/열 최대 갱신
    max_row = max(max_row, row_sum)
    max_col = max(max_col, col_sum)

    # 다음 단계 재귀 호출
    return arc(idx + 1, arr, n, max_row, max_col, cross1, cross2)

T = 10
for tc in range(1, T + 1):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = arc(0, arr, 100)
    print(f'#{tc}', result)