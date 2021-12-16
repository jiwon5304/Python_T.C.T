# 선택 정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    # 가장 작은 원소의 인덱스
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 삽입 정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    # 인덱스 i 부터 1까지 1씩 감소하며 반복하는 문법
    for j in range(i,0,-1):
        # 한 칸씩 왼쪽으로 이동
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)

# 퀵 정렬
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 떄까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if(left > right):
            array[right], array[pivot], = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)
print(array)

# 간결한 퀵 정렬
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만들 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼족 부분과 오른족 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

# 각 데이터에 해당하는 인덱스의 값 증가
for i in range(len(array)):
    count[array[i]] += 1

# 리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
        print(i, end=' ')

# 선택정렬과 기본정렬 라이브러리 수행 시간 비교
from random import randint
import time

# 배열에 10,000개의 정수삽입
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1,100))

# 선택 정렬프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

# 측정 종료
end_time = time.time()

# 수행시간 출력
print('선택정렬 성능 측정:', end_time-start_time)

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1,100))

# 기본정렬 라이브러리 성능 측정
start_time = time.time()

# 기본정렬 라이브러리 
array.sort()

# 측정 종료
end_time = time.time()

# 수행시간 출력
print('기본정렬 라이브러리 성능 측정:', end_time-start_time)

