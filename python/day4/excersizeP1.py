fileName = input('백업 저장할 파일 명을 입력하세요 : ')

with open(fileName,'r',encoding='utf=8') as origin:

    contents = origin.read()
    with open(fileName + '.bak','w',encoding='utf-8') as backUp:
        backUp.write(contents)

print('백업을 저장했습니다.')

    
