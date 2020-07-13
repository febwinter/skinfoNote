'''
버블 정렬

리스트 한쪽 끝부터 요소들을 비교해 정렬하며
시작한 쪽은 정렬되지 않은 리스트, 진행 방향쪽은 정렬된 리스트로 구성된다.

'''

def bubble_sort(L:list)->list:

    for i in range(0,len(L) - 1):
        for j in range(0, len(L) - 1 - i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    
    return L


L = [9,8,7,6,54,3,1]

L = bubble_sort(L)

print(L)