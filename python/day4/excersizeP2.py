alkalineMetals = []

with open('alkaline_metals.txt','r',encoding='utf-8') as alk:
    
    for line in alk:
        line = line.strip()
        temp = line.split(' ')
        alkalineMetals.append(temp)
    
print(alkalineMetals)