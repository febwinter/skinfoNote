name = ['A','B','C']
kor = [100, 90, 80]
eng = [80, 90, 70]
mat = [50, 60, 70]

for i in range(len(name)): #
    print(name[i])
    total = kor[i] + eng[i] + mat[i]
    avg = total / 3