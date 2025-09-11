# # Lv.1 factorial
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     elif n < 0:
#         return 'negative'
#     else:
#         return n*factorial(n-1)
#
#
# # factorial(1)
# print(factorial(-1))




# # Lv.2 전체 배열의 합
# def calc(arr):
#     if not arr:
#         return 0
#     return arr[0] +calc(arr[1:])
# list_a = [1,2,3,4,5]
# print(calc(list_a))



# # Lv.3 복잡한 규칙 적용하기 (최대공약수)
# def GCD(a, b):
#     if b == 0:
#         return a
#     return GCD(b , a % b)
# print(GCD(24,16))
# print(GCD(7,3))




# # Lv.4 여러 갈래로 쪼개기 (피보나치)
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# for i in range(8):
#     print(fibo(i), end= ' ')





# # Lv.5 복합적인 문제 해결 (하노이의 탑)
# def hanoi_tower(n, from_pole, to_pole, aux_pole):
#     if n == 1:
#         print(f"Move disk from {from_pole} to {to_pole}")
#         return
#     hanoi_tower(n - 1, from_pole, aux_pole, to_pole)
#     print(f"Move disk from {from_pole} to {to_pole}")
#     hanoi_tower(n - 1, aux_pole, to_pole, from_pole)
#
# # --- 실행 예시 ---
# N = 3
# hanoi_tower(N, 'A', 'C', 'B')





# def factorial(n):
#     # 함수가 어떤 인자로 호출되었는지 출력
#     print(f"factorial({n}) 호출됨")
#
#     if n <= 1:
#         # 기저 조건에 도달했음을 알림
#         print(f"기저 조건 도달! 1 반환")
#         return 1
#
#     result = n * factorial(n - 1)
#
#     # 함수가 어떤 값을 반환하는지 출력
#     print(f"factorial({n})에서 {result} 반환") # 이 부분은 재귀가 끝나고 나서 출력. 역순으로
#     return result
#
# factorial(3)


# def calc(n):
#     if n == 1:
#         return 1
#     else:
#         return n + calc(n-1)
# print(calc(5))

# N = int(input())
#
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
# for i in range(N):
#     if i == N-1:
#         print(fibo(i))



def recursion(s, l, r):
    if l >=r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)

def palindrome(s):
    return recursion(s, 0, len(s)-1)

print(palindrome('ABCBA'))
print(palindrome('ABC'))





















































