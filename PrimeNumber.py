import math


def is_prime(number):
    prime = True
    for i in range(2,int(math.sqrt(number))+1):
        if number % i ==0:
            prime = False 
    return prime
    

counter = 0
for i in range(2,200000000):
    if is_prime(i):
        counter += 1
        if counter == 10001:
            print(i)
            break
