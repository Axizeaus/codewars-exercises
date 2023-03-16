# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    i = 0
    multiples = [] 
    while(i < number):
        if (( i % 3 == 0) and (i % 5 == 0)):
            multiples.append(i)
        elif (i % 5 == 0):
            multiples.append(i)
        elif (i % 3 == 0):
            multiples.append(i)
        i += 1
    sum = 0
    for i in multiples:
        sum += i
    return sum