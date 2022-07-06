# heapq => min_heap이 기본, 음수로 바꿔서 max_heap 사용

# 삽입 : heapq.heappush()
# 추출 : heapq.heappop()

# Heap Sort
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value) # -value : max_heap
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(heapq.heappop(h)) # -heapq.heappop(h) : max_heap
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)