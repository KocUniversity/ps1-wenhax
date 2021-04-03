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

# Brute Force Search
T = 1
flag = 1
answer = -1
while T < 10001 and flag == 1:
    if formula * T > B:
        answer = T
        flag = 0
    else:
        T = T+1

print(answer)