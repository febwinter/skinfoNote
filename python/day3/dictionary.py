countryCode = {}
countryCode = {'America':'1','Austrailia':'61','Japan':'81','Korea':'82','China':'86'}

print(countryCode)

countryCode['Germany'] = '49' # 새로운 key, value 추가


print(countryCode.keys()) # key값들은 list 형태로 나타나게 된다.
print(countryCode.values()) # value 값들도 list 형태로 나타나게 된다.

print(countryCode.items()) # dictionary가 tuple 묶음으로 된 list 형태로 출력된다.
print()


# method1
for items in countryCode.items():
    k, v = items # unpackaging
    #print(items) # key, value
    print(items,k,v)

print()

# method2 << unpacking >>
for k, v in countryCode.items():
        print(k,v)
