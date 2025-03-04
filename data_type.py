"""
파이썬에서 사용하는 데이터 타입(object) 정리
1.1 가변성 (Mutable vs. Immutable)
가변(Mutable) 데이터 타입: 값을 변경할 수 있음 (리스트, 딕셔너리 등)
불변(Immutable) 데이터 타입: 값을 변경할 수 없음 (정수, 문자열, 튜플 등)

1.2 동질성 (Homogeneous vs. Heterogeneous)
Homogeneous (동질적): 같은 타입의 요소만 포함하는 구조 (예: array.array, bytes)
Heterogeneous (이질적): 서로 다른 타입의 요소를 포함할 수 있음 (예: 리스트, 튜플, 딕셔너리)

1.3 시퀀스 (Sequence vs. Non-Sequence)
Sequence (순서 O): 인덱싱과 슬라이싱이 가능한 데이터 타입 (예: 리스트, 튜플, 문자열)
Non-Sequence (순서 X): 인덱싱이 불가능한 데이터 타입 (예: 집합, 딕셔너리)
시퀀스의 경우 (*3) 복사: [1, 2, 3] * 3 -> [1, 2, 3, 1, 2, 3, 1, 2, 3]

바인딩(Binding)
a=b=1
a = b = [1, 2, 3]
b.append(4)
a -> [1, 2, 3, 4]

Packing vs Unpacking
여러 개의 값을 하나의 변수(컬렉션)로 묶는 것
하나의 컬렉션(리스트, 튜플 등)에 있는 여러 값을 개별 변수에 할당하는 것
* 언패킹: 리스트/튜플을 개별 인자로 함수에 전달	
** 언패킹: 딕셔너리를 키워드 인자로 함수에 전달	

"""

# 정수 (Integer)
# 값의 제한이 없다!
# 무한대의 경우 a == a+1의 케이스가 생김
integer_example = 42
print("정수 (Integer):", integer_example, "타입:", type(integer_example))

# 실수 (Float)
# 실수의 연산은 정확하지 않을 수 있다!
# 0.1 + 0.1 + 0.1 = 0.30000000001??
float_example = 3.14159
print("실수 (Float):", float_example, "타입:", type(float_example))

# 문자열 (String)
string_example = "Hello, Python!"
print("문자열 (String):", string_example, "타입:", type(string_example))

# 불리언 (Boolean): True는 1, False는 0
a = True
b = True
a + b # 2
boolean_example = True
print("불리언 (Boolean):", boolean_example, "타입:", type(boolean_example))

# 리스트 (List)
list_example = [1, 2, 3, "Python", 3.14]
print("리스트 (List):", list_example, "타입:", type(list_example))

# 튜플 (Tuple)
tuple_literal = 1, 2, 3
print(tuple_literal)
tuple_example = (1, 2, 3, "Python", 3.14)
print("튜플 (Tuple):", tuple_example, "타입:", type(tuple_example))

# 딕셔너리 (Dictionary)
# Dictionary View(dict.keys(), dict.values(), dict.items()): 딕셔너리의 키, 값 또는 (키, 값) 쌍을 동적으로 반환하는 객체
dict_example = {"name": "Alice", "age": 30, "language": "Python"}
print("딕셔너리 (Dictionary):", dict_example, "타입:", type(dict_example))

# 집합 (Set)
empty_set = set()
set_example = {1, 2, 3, "Python", 3.14}
print("집합 (Set):", set_example, "타입:", type(set_example))

# bytearray
# 바이트(byte) 단위의 가변(mutable) 시퀀스를 나타내는 파이썬의 내장 데이터 타입
ba = bytearray(5)
ba = bytearray([65, 66, 67])
print(ba) 