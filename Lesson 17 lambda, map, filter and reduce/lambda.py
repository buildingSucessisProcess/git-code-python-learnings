squared = lambda num : num * num 
#def squared(num): return num * num --> exactly the same as above

print(squared(2))

addTwo = lambda num : num + 2
print(addTwo(12))

sum_total = lambda a, b : a + b

print(sum_total(10, 8))


##############################################################
#when would I use lambda

def funcBuilder(x):
    return lambda num : num + x #returning of a function as lambda is a function

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

###############################################################
#Higher order function:
# returns a function or takes one or more functions as arguments



numbers = [3,7,12,18,20,21]

#map receives a function as a first argument, as a second a list and iterates through the list
#like a loop but way more efficient
squared_nums = map(lambda num : num * num, numbers) 

print(list(squared_nums))

##############################################################
#filter

#lambda num : num % 2 != 0 --> divides a number by 2 and keeps only the decimal part, if its not 0

odd_nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_nums))

##############################################################

from functools import reduce

lambda acc, curr: acc + curr #take the accumulated number and add it to the current (in the iteration)

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))

#lambda acc, curr : acc + len(curr) --> accumulate length to a current value

names = ['Dave Gray','Sara Ito','John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0) #with the 0 we tell its about nr

print(char_count)
