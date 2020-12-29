# PRACTICAL 4
"""
Writing  a program that reads a file “myfile.txt” and builds a histogram
(a dictionary having key value pair as word: occurrence) of the words in the file.

a) Now use histogram to print-
    i) Total number of words
    ii) Number of different words
    iii) The most common words

b) Using  above text file “myfile.txt”, write a program that maps a list of words
read from the file to an integer representing the length of the corresponding words.
(use dictionary having key value pair as  length : list of word )
Now using above dictionary design a function find_longest_word() to display a list of longest words from file.
Define a function filter_long_words(n) that takes an integer n and returns the list
of words that are longer than n from file.
"""
path = '/content/drive/My Drive/Shared with me/test_set/myfile.txt'
try:
    f = open(path)
    f.close()
except FileNotFoundError:
    print('Checking local path...')
    path = 'myfile.txt'


def __a__():
    with open(path) as f:
        p = (' '.join(f.read().split('\n'))).strip().split(' ')
        freq = {}
        for i in p:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        print(freq)
        print(f'a)\ni)Total no. of words:\n{sum(freq.values())}')  # -->a) i)
        print(f'ii)No. of different words:\n{len(freq)}')  # --> a) ii)
        print('iii)Most common word:\n', *
              [x for x in freq if freq[x] == max(freq.values())])  # -->


__a__()


def __b__():
    freq = freq_create()
    print('Longest words in file:\n', *[freq[x]
                                        for x in freq if x == max(freq.keys())])
    filter_long_words(
        freq, input('Enter value for which you want to filter:'))  # --> b)


def freq_create():
    with open(path) as f:
        p = (' '.join(f.read().split('\n'))).strip().split(' ')
        freq = {}
        for i in p:
            if len(i) not in freq:
                freq[len(i)] = [i]
            elif i not in freq[len(i)]:
                freq[len(i)] += [i]
        return freq


def filter_long_words(freq, n):  # -->b)
    print(*[freq[_] for _ in freq if _ > int(n)], sep='\n')


__b__()
