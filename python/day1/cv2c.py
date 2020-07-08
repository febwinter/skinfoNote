def convert_to_celsius(temp):
    result = (temp - 32) * 5 / 9
    print('result : ', result)
    return result

def add(x,y):
    result = x + y
    # print(result)
    return result

convert_to_celsius(212)
sum = add(100,200)
print('100 + 200 = ', sum)