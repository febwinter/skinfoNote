import urllib.request
total_pelts = 0
url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)
        
        if line.startswith('#'):
            continue
        
        try: # 예외처리
            total_pelts += int(line)
        except: # 오류 발생시 실행
            continue

print('Total number of pelts: {}'.format(total_pelts))