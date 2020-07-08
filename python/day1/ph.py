# ph = float(input('pH 농도를 입력하세요 : '))
# if ph < 7.0:
#     print('{}은(는) 산성입니다.'.format(ph))
# elif ph > 7.0:
#     print('{}은(는) 염기성입니다.'.format(ph))
# else:
#     print('{}은(는) 중성입니다.'.format(ph))


value = input('pH 농도를 입력하세요: ')
if len(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print('{}은(는) 산성입니다.'.format(ph))
    elif ph > 7.0:
        print('{}은(는) 염기성입니다.'.format(ph))
    else:
        print('{}은(는) 중성입니다.'.format(ph))
else:
    print('농도를 입력하지 않았습니다.')
