# 다익스트라 알고리즘
from queue import PriorityQueue
import heapq

def sort_path(path:dict)->dict: # 각 장소별 거리값을 거리값 기준으로 오름차순으로 정렬해주는 함수
    return dict(sorted(path.items(), key=lambda u: u[1]))

# 최장거리보다 큰 경로를 계산해주는 함수
def makeInf(paht:dict)->int:
    length = [] # 최장거리 구해 inf 값 설정하기
    for route in path.values():
        length.extend(list(route.values()))
    return max(length) + 10 # 현재 값에서 가장 긴 길의 가중치는 11이고 이에 따른 inf 값은 21이다 

# 경로
path = { "집": {"미용실":5, "슈퍼마켓":10, "학원":9}, "미용실": {"집":5, "슈퍼마켓": 3, "은행":11}, "슈퍼마켓": {"집":10, "미용실":3, "레스토랑":3, "은행":10, "학원":7}, "학원": {"집":9, "슈퍼마켓":7, "커피숍":8}, "은행": {"미용실":11, "슈퍼마켓":10, "커피숍":5}, "레스토랑": {"슈퍼마켓":3, "커피숍":3}, "커피숍": {"레스토랑":3, "은행":5, "학원":8} }

# 방향 그래프

end = input('도착지를 입력하시오 : ')

start = '집'
inf = makeInf(path) # inf 값 생성

# dist = {vertex: [inf, start] for vertex in path}
dist = {vertex: inf for vertex in path}
print(dist)

# 그래프의 시작 정점의 거리는 0으로 초기화 해줌
dist[start] = [0, start]

# 모든 정점이 저장될 큐를 생성합니다.
queue = []

# 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
heapq.heappush(queue, [dist[start][0], start])

while queue:
    
    # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
    current_distance, current_vertex = heapq.heappop(queue)
    
    # 더 짧은 경로가 있다면 무시한다.
    if dist[current_vertex][0] < current_distance:
        continue
        
    for adjacent, weight in path[current_vertex].items():
        distance = current_distance + weight
        # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
        if distance < dist[adjacent][0]:
            # 거리를 업데이트합니다.
            dist[adjacent] = [distance, current_vertex]
            heapq.heappush(queue, [distance, adjacent])

path = end
path_output = end + '->'
while dist[path][1] != start:
    path_output += dist[path][1] + '->'
    path = dist[path][1]
path_output += start
print (path_output)
print(dist)



# numPlaces = len(path) # 장소의 갯수



# # 최단거리 저장용 dictionary 변수
# spots = list(path.values())
# dist = {place: [inf] for place in spots}

# print(dist)











