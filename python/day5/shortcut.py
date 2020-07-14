# 다익스트라 알고리즘
from queue import Queue

# place 에 연결된 
def sortPath(path: dict, place: str)->dict: 
    return dict(sorted(path[place].items(), key=lambda u: u[1])) # ex) {'미용실':5, '슈퍼마켓':10, '학원':9 }

# 최장거리보다 큰 경로를 계산해주는 함수
def makeInf(paht:dict)->int:
    length = [] # 최장거리 구해 inf 값 설정하기
    for route in path.values():
        length.extend(list(route.values()))
    return max(length) + 10 # 현재 값에서 가장 긴 길의 가중치는 11이고 이에 따른 inf 값은 21이다 

def dijkstra(path: dict, start, end)->int or str:

    # inf = makeInf(path) # inf 값 생성

    # 최단거리 저장을 위한 dist 생성
    #dist = {vertex: inf for vertex in path}
    dist = {vertex: 'inf' for vertex in path}

    # 계산한 노드인지 체크하기 위한 dict 생성
    # False = 체크하지 않은 노드, True = 체크한 노드
    nodeCheck = {vertex: False for vertex in path}
    nodeCheck[start] = False

    # 다음 계산할 노드를 저장하기 위한 queue 생성
    nodeQueue = Queue()

    nodeQueue.put(start) # 출발지점 이름을 큐에 집어넣는다.
    nodeCheck[start] = True # 출발지점을 확인했음을 체크한다.
    dist[start] = 0 # 출발지 -> 출발지 최단거리를 0으로 설정한다.

    while nodeQueue.empty() != True:

        # 큐 내용물을 하나 꺼낸다.
        nodeName = nodeQueue.get()
        tempPath = sortPath(path,nodeName)

        for key, value in tempPath.items(): # 꺼낸 노드와 연결된 노드를 경로가 짧은 순서대로 이름을 넣는다.
            if nodeCheck[key] != True: # 이미 확인한 노드인 경우 건너뛴다
                nodeQueue.put(key)
                nodeCheck[key] = True # 큐에 넣은 노드를 체크한다.
        
            # 최단거리 계산 : min(dist[A] + D[A][B], dist[B]) (현재 노드까지 최단거리 + 다음 노드까지 거리와 기존 다음 노드까지 최단거리)
            if value == 'inf':
                continue
            elif dist[key] == 'inf':
                dist[key] = dist[nodeName] + value
            else:
                dist[key] = min(dist[nodeName] + value, dist[key])
    if dist[end] == 'inf':
        return "경로가 없습니다"
    else:
        return dist[end]
# 경로
path = { "집": {"미용실":5, "슈퍼마켓":10, "학원":9}, "미용실": {"집":5, "슈퍼마켓": 3, "은행":11}, "슈퍼마켓": {"집":10, "미용실":3, "레스토랑":3, "은행":10, "학원":7}, "학원": {"집":9, "슈퍼마켓":7, "커피숍":8}, "은행": {"미용실":11, "슈퍼마켓":10, "커피숍":5}, "레스토랑": {"슈퍼마켓":3, "커피숍":3}, "커피숍": {"레스토랑":3, "은행":5, "학원":8} }

# path = {'집':{'학원':1},'학원':{'식당':3,'카페':8},'식당':{'집':2,'레스토랑':4,'카페':7},'레스토랑':{'식당':5,'카페':6},'카페':{}}

# 출발지와 도착지를 결정
while True:
    try:
        start = input('출발지를 입력하시오 : ')
        list(path.keys()).index(start)
        end = input('도착지를 입력하시오 : ')
        list(path.keys()).index(end)
        break

    except:
        print('존재하는 값을 입력하세요')

shortcut = dijkstra(path, start, end)

print('{}부터 {}까지의 최단 경로의 길이는 {}이다.'.format(start, end, shortcut))