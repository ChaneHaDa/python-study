"""
closure??
내부 함수가 외부 함수의 변수에 접근할 수 있도록 그 환경을 함께 저장한 함수
"""

# 예시1
# 외부 함수
def make_adder(x):
    # 내부 함수
    # x -> 자유 변수, 지정해준 값을 계속 기억함
    def adder(y):
        return x + y
    return adder

add_10 = make_adder(10)
print(add_10(5))
print(add_10(20)) 

# 예시2
def unique_id_generator(prefix):
    counter = 0  # 내부 상태, 클로저가 기억할 변수
    
    def generate():
        nonlocal counter  # 외부 변수 counter를 사용하기 위해 nonlocal 선언
        counter += 1
        return f"{prefix}{counter}"
    
    return generate

# 클로저를 사용해 유니크 ID 생성기 생성
id_gen = unique_id_generator("User_")

print(id_gen())  # 출력: User_1
print(id_gen())  # 출력: User_2
print(id_gen())  # 출력: User_3