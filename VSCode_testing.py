sieve = [True]*101
print(sieve)
for i in range(2,100):
    if sieve[i]:
        print(i)
        for j in range(i*i, 100, i):
            sieve[j] = False
            print("i am the false position: " + str(j))