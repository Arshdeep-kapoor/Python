initialPopu = 312032486
time = 365*24*60*60

population = initialPopu+(time//7)-(time//13)+(time//45)
initialPopu = population
print(initialPopu,  " population after 1st year")
    
population = initialPopu+(time//7)-(time//13)+(time//45)
initialPopu = population
print(initialPopu,  " population after 2nd year")

population = initialPopu+(time//7)-(time//13)+(time//45)
initialPopu = population
print(initialPopu,  " population after 3rd year")

population = initialPopu+(time//7)-(time//13)+(time//45)
initialPopu = population
print(initialPopu,  " population after 4th year")

population = initialPopu+(time//7)-(time//13)+(time//45)
initialPopu = population
print(initialPopu,  " population after 5th year")