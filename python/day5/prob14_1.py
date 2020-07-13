"""
국가명, 인구 면적으로 한 국가를 표현하는 Country 클래스 구현
"""

class Country():
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
    
    def __str__(self):
        return '{} has population {} and is {} square km.\n'.format(self.name, self.population, self.area)

    def population_density(self):
        return self.population / self.area
    
