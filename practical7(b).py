def function(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find(n):
    prime = []
    num = 2
    while len(prime) < n:
        if function(num):
            prime.append(num)
        num += 1
    return prime

n = 10
prime = find(n)
print("The first", n, "prime numbers are:")
print(prime)
