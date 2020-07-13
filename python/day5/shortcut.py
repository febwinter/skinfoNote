# 다익스트라 알고리즘
from queue import Queue
from queue import PriorityQueue
import heapq

# place 에 연결된 
def sortPath(path: dict, place: str)->dict: 
    return sorted(path[place], key=lambda u: u[1]) # ex) {'미용실':5, '슈퍼마켓':10, '학원':9 }

# 최장거리보다 큰 경로를 계산해주는 함수
def makeInf(paht:dict)->int:
    length = [] # 최장거리 구해 inf 값 설정하기
    for route in path.values():
        length.extend(list(route.values()))
    return max(length) + 10 # 현재 값에서 가장 긴 길의 가중치는 11이고 이에 따른 inf 값은 21이다 

def dijkstra(path: dict, start, end)->int:

    inf = makeInf(path) # inf 값 생성

    # 최단거리 저장을 위한 dist 생성
    dist = {vertex: inf for vertex in path}

    # 계산한 노드인지 체크하기 위한 dict 생성
    # False = 체크하지 않은 노드, True = 체크한 노드
    nodeCheck = {vertex: False for vertex in path}
    nodeCheck[start] = False

    # 다음 계산할 노드를 저장하기 위한 queue 생성
    nodeQueue = Queue()

    nodeQueue.put(start) # 출발지점 이름을 큐에 집어넣는다.
    nodeCheck[start] = True
    dist[start] = 0 # 출발지 -> 출발지 최단거리를 0으로 설정한다.

    while nodeQueue.empty() != True:

        # 큐 내용물을 하나 꺼낸다.
        nodeName = nodeQueue.get()
        tempPath = sortPath(path,nodeName)

        for key, value in tempPath.items: # 꺼낸 노드와 연결된 노드를 경로가 짧은 순서대로 이름을 넣는다.
            nodeQueue.put(key)
            nodeCheck[key] = True # 큐에 넣은 노드를 체크한다.
        
            # 최단거리 계산 : min(dist[A] + D[A][B], dist[B]) (현재 노드까지 최단거리 + 다음 노드까지 거리와 기존 다음 노드까지 최단거리)
            dist[key] = min(dist[nodeName] + value, dist[key])

    return dist[end]

# 경로
path = { "집": {"미용실":5, "슈퍼마켓":10, "학원":9}, "미용실": {"집":5, "슈퍼마켓": 3, "은행":11}, "슈퍼마켓": {"집":10, "미용실":3, "레스토랑":3, "은행":10, "학원":7}, "학원": {"집":9, "슈퍼마켓":7, "커피숍":8}, "은행": {"미용실":11, "슈퍼마켓":10, "커피숍":5}, "레스토랑": {"슈퍼마켓":3, "커피숍":3}, "커피숍": {"레스토랑":3, "은행":5, "학원":8} }

# 출발지와 도착지를 결정
while True:
    try:
        start = input('출발지를 입력하시오 : ')
        list(path.keys).index(start)
        end = input('도착지를 입력하시오 : ')
        list(path.keys).index(end)
        break

    except:
        print('존재하는 값을 입력하세요')

shortcut = dijkstra(path, start, end)

print('{}부터 {}까지의 최단 경로의 길이는 {}이다.'.format(start, end, shortcut))






# # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
# dist[start] = [0, start]

# # 모든 정점이 저장될 큐를 생성합니다.
# queue = []

# # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
# heapq.heappush(queue, [dist[start][0], start])

# while queue:
    
#     # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
#     current_distance, current_vertex = heapq.heappop(queue)
    
#     # 더 짧은 경로가 있다면 무시한다.
#     if dist[current_vertex][0] < current_distance:
#         continue
        
#     for adjacent, weight in path[current_vertex].items():
#         distance = current_distance + weight
#         # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
#         if distance < dist[adjacent][0]:
#             # 거리를 업데이트합니다.
#             dist[adjacent] = [distance, current_vertex]
#             heapq.heappush(queue, [distance, adjacent])

# path = end
# path_output = end + '->'
# while dist[path][1] != start:
#     path_output += dist[path][1] + '->'
#     path = dist[path][1]
# path_output += start
# print (path_output)
# print(dist)



# numPlaces = len(path) # 장소의 갯수



# # 최단거리 저장용 dictionary 변수
# spots = list(path.values())
# dist = {place: [inf] for place in spots}

# print(dist)











