s = 'C3H7'
total = 0
count = 0

for i in range(len(s)):
    if s[i].isalpha(): # 문자인지 확인하는 str 매서드
        continue
    total += int(s[i])
    count += 1

print(total)
print()
print(count)