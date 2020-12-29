# PRACTICAL 2
"""
? Taking file1.txt containing some text and writing  a function named isvowel( ) that reads
? the file file2-1.txt and creates a new file named file2-2.txt, which shall contain only those
? words from the file file2-1.txt  which don’t start with a vowel
"""

# ! Why is this here? (Corona2020- Everyone was using GoogleColab and that needed some special configs to get this to work)
# TODO: Remove this path and switch to normal script.
path = '/content/drive/My Drive/test_set/Shared with me/file2-1.txt'

try:
    f = open(path)
    f.close()
except FileNotFoundError:
    print('Checking local path...')
    path = 'file2-1.txt'

with open(path) as fl:
    p = fl.readlines()
    print('Text read from file1:\n', *p)
    for i in p:
        k = i.strip().split(' ')
        nl = []
        for j in k:
            if j[0].lower() not in 'aeiou':
                nl.append(j)
            else:
                continue
        nl = ' '.join(nl) + '\n'

        with open('file2-2.txt', 'w') as fl2:
            fl2.write(nl)

    with open('file2-2.txt') as fl2:
        print('Text added to  file2:\n', fl2.read())
