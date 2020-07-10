with open('hopedale.txt','r') as hopedale_file:
    hopedale_file.readline()

    data = hopedale_file.readline().strip()
    while data.startswith('#'):
        data = hopedale_file.readline().strip()

    total_pelts = int(data)

    for data in hopedale_file:
        total_pelts = total_pelts + int(data.strip())
    
print('Total number of pelts: {}'.format(total_pelts))