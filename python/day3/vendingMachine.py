products = {'커피' : 300, '생수':100,'쥬스':700,'우유':200}
returnMoney = 0
money = 0
looper = True
cnt = 0
nameList = []
while looper:

    try:
        if money == 0:
            print('커피(300원), 생수(100원), 쥬스(700원), 우유(200원)를 선택하실 수 있습니다.')
            money = int(input('돈을 넣으세요 -> '))
        
        if money < 100:
            print('돈이 너무 적습니다.')
            raise Exception

        for name, val in products.items():
            
            if(val <= money):
                print('{}({}원) '.format(name, val),end ='')

        print('를 선택하실 수 있습니다.')
        prod = input('음료를 선택하세요 -> ')

        if prod != '커피' and prod != '생수' and prod != '쥬스' and prod != '우유':
            raise Exception
        if money < products[prod]:
            raise Exception

    except:
        print('범위 내에서 선택해 주세요')
        print()

    else:
        returnMoney = money - products[prod]
        print('{} 를 선택하셨습니다. 거스름돈은 {}원 입니다.'.format(prod,returnMoney))
        print()
        
        while True:
            try:
                ans = input('추가 주문을 하시겠습니까? (Y/N) -> ')

                if ans != 'Y' and ans != 'N':
                    raise Exception
            except:
                print('Y / N 로 답하세요!')
                continue
            else:
                if ans == 'Y':
                    break
                else:
                    looper = False
                    break

print('주문이 완료되었습니다.')