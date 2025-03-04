"""
Python 비교 연산자 정리

비교 연산자는 두 값을 비교하여 불리언 값(True 또는 False)을 반환합니다.

연산자 | 의미
-------|-------
==     | 두 값이 같으면 True
!=     | 두 값이 다르면 True
<      | 왼쪽 값이 오른쪽 값보다 작으면 True
<=     | 왼쪽 값이 오른쪽 값보다 작거나 같으면 True
>      | 왼쪽 값이 오른쪽 값보다 크면 True
>=     | 왼쪽 값이 오른쪽 값보다 크거나 같으면 True
"""


a, b = 10, 20

print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a < b:", a < b)    # True
print("a <= b:", a <= b)  # True
print("a > b:", a > b)    # False
print("a >= b:", a >= b)  # False

# 문자열 비교 (ASCII 값 기준)
print("'apple' < 'banana':", 'apple' < 'banana')  # True ('a' vs 'b')

# 리스트 비교 (첫 번째 요소부터 순차적으로 비교)
print("[1, 2, 3] < [1, 2, 4]:", [1, 2, 3] < [1, 2, 4])  # True (3 vs 4)

# 튜플 비교
print("(1, 2) > (1, 1):", (1, 2) > (1, 1))  # True (2 vs 1)

# 불리언 비교 (True는 1, False는 0과 동일)
print("True == 1:", True == 1)  # True
print("False == 0:", False == 0)  # True