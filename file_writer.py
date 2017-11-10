# Ruby does this so much better. This was a pain.
f = open('test_file.txt', 'w')
f.write('This is a test file.\n'
        'This is the second line.\n'
        'This is the third line.\n')
f.close()
f = open('test_file.txt', 'r')
for line in f:
    print(line, end='')
f.close
f.closed
