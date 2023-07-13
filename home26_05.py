
#number1
"""
def kilo_pound(kilo):
    pound = kilo/2.2
    return pound
kilo = int(input("Please enter your weight in kilograms!"))
p = kilo_pound(kilo)
print(f"Your weight in pounds:", p)
"""
#number 3
"""
def calculate(x , y):
    
    result=abs(x-y)/(x+y)
    return result
x = float(input("Please , enter x."))
y = float(input("Please, enter y."))
res = calculate(x , y)
print(f"Your result is:", res)
"""
#number 2
"""
import random
def randomm():

    for i in range(1,51):
        random_num=random.randrange(3,6)
        print(random_num)
randomm()
"""
#number 4
"""
def years():
    sum = 0
    for i in range(1600, 2024):
        if i % 100 == 0 and i % 400 == 0:
            sum += 1   
        elif i%4 ==0:
            sum += 1
    return sum          
result = years()
print(result)
"""
#number 5

for i in range(6, 10001):
    total_sum=0
    j=1
    while j<=i/2:
        if i % j == 0:
            total_sum += j
        j += 1
    if total_sum == i:
        print(i)

