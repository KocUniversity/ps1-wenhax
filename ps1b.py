import math
n = input("Enter number of elements: ")
n = int(n)
B = input("Enter lower bound: ")
B = int(B)

# Formula Calculation
formula = 0
for i in range(1, n+1):
    if (i % 2) == 0:
        p = 2**i+1
    else:
        p = 3**i+1
    formula = formula + p**(n-i)

# Bisection Search
min_t = 1
max_t = 10000
guess = math.ceil((min_t + max_t) * 0.5)
answer = -1

while max_t >= min_t:
    if formula * guess > B:
        answer = guess
        max_t = guess-1
        guess = math.ceil((min_t + max_t) * 0.5)
    else:
        min_t = guess + 1
        guess = math.ceil((min_t + max_t) * 0.5)

print(answer)