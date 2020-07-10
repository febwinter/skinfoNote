file = open('my_recipe.txt','a',encoding='utf-8')
print(type(file))
text = """* 라면 레시피
1. 물을 끓인다.
2. 라면과 스프를 넣는다.
3. 5분을 더 끓은 후에 먹는다.
"""
file.write(text)
file.close()
