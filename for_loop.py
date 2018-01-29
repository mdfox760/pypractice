for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print (n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number.')

# continue statement
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number.", num)
    break

else:
    print("I found nothing!")

knights = {'Gallahad': 'the pure', 'Robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding
# value can be retrieved at the same time using teh enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries
# can be paired with the zip function.
questions = ['name', 'quest', 'favorite color']
answers = ['Lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
