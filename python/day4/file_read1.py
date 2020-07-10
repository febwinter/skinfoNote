'''
filename : fileread1.py
'''
file = open('file_example.txt','r',encoding='utf-8')

'''
2 Byte 문자의 경우 utf-8로 인코딩되어 저장된다.
file open시에 윈도우의 경우 cp949로 읽어오기 때문에 utf-8 파일을 cp949로 읽어오면 오류가 발생하게된다.
따라서 open 매서드에 encoding = 'utf-8 옵션을 추가해준다.
'''

'''
print(file) # 파일 내용을 출려해주는 것이 아니라 python 오브젝트(class)에 대한 내용을 출력한다.

contents = file.read() # 현재 불러올 파일의 형태는 UTF-8
'''

# with를 사용하면 가독성을 높일 수 있다.

with open('file_example.txt','r',encoding='utf-8') as file:
    print(file)
    contents = file.read()


print(contents)

# 오류 때문에 close()가 실행이 안되는 경우가 있다.
file.close()

