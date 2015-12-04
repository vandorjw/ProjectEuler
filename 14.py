
def collatz(n, count):
    if n == 1:
        return count
    else:
        count = count + 1
        if n % 2 == 0:
            n = n /2
        else:
            n = 3 * n + 1
        return collatz(n, count)

max_collatz = 1
iteration = 1

for i in range(1, 1000000):
    count = 1
    contesting = collatz(i, 1)

    if contesting > max_collatz:
        max_collatz = contesting
        iteration = i


print("Final winner is integer {}".format(iteration))
