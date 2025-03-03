import time

# 예시1: 실행 시간 측정
def elapsed(original_func): # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func() # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

myfunc()

# 예시2: 로깅 작성
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] 함수 {func.__name__} 호출됨")
        result = func(*args, **kwargs)
        print(f"[DEBUG] 함수 {func.__name__} 종료됨")
        return result
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")