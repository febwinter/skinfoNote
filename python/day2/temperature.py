def convert_to_celsius(temp: float) -> float:
    result = (temp - 32) * 5 / 9
    print('result : ', result)
    return result

def above_freezing(celsius: float) -> bool:
    return celsius > 0