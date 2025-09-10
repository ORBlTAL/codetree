
import sys
sys.stdin = open('input2.txt')
N , M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = list(map(list, zip(*arr)))
temp1 = temp2 = 0
if M == 1:
    print(2*N)
else:
    for j in range(N):
        cnt1 = 0
        for i in range(len(arr)-1):
            if arr[j][i] == arr[j][i+1]:
                cnt1 +=1
            # print(cnt1)
                if cnt1 >= M - 1:
                    temp1+=1
                    break
            else:
                cnt1 = 0
# print(temp1)
    for j in range(N):
        cnt2 = 0
        for i in range(len(arr)-1):
            if arr2[j][i] == arr2[j][i+1]:
                cnt2 +=1
            # print(cnt2)
                if cnt2 >= M - 1:
                    temp2+=1
                    break
            else:
                cnt2 = 0
# print(temp2)
    print(temp1+temp2)