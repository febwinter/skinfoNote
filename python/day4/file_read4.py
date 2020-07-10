from io import StringIO

input_string = '1.3 3.4\n2 4.2\n-1 1\n'
print(input_string)

infile = StringIO(input_string) # StringIO를 통해 문자열을 파일 오브젝트로 변환한다.

print(infile.readline())