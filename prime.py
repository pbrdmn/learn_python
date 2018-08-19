x = int(input('Enter a number: '))
half = int(x / 2)
prime = True

for i in range(2, half):
    if x % i == 0:
        print(x, '=', i, '*', x//i)
        prime = False
        break

if (prime):
    print(x, 'is prime')
