# PRACTICAL 1
"""
 * Writing a function to create a text file containing following data:

 * Neither apple nor pine are in pineapple. Boxing rings are square.
 * Writers write, but fingers don’t fing. Overlook and oversee are opposites.
 * A house can burn up as it burns down. An alarm goes off by going on.
 * AND
 ? a)Reading back the entire file content using read( ) or readlines( ) and displaying.
 ? b)Appending more text of your choice in the file and display the content of file with line numbers prefixed to line.
 ? c)Displaying last line of file.
 ? d)Displaying first line from 10th character onwards.
 ? e)Reading and displaying a line from the file. Ask user to provide the line number to be read.
 ? f)Finding the frequency of words beginning with every letter.
 ! The 'fing' typo was in the question, not done by me xD
"""

# ! Why is this here? (Corona2020- Everyone was using GoogleColab and that needed some special configs to get this to work)
# TODO: Remove this path and switch to normal script.
path = '/content/drive/My Drive/test_set/Shared with me/file1.txt'


def fl_create_ql(env_path):
    # TODO: documentation
    try:
        with open(env_path, 'w+') as fl:
            fl.writelines(
                [
                    'Neither apple nor pine are in pineapple. Boxing rings are square.\n',
                    'Writers write, but fingers don\'t fing. Overlook and oversee are opposites.\n',
                    'A house can burn up as it burns down. An alarm goes off by going on.'])
            fl.seek(0)
            print(f'a)\n{fl.read().strip()}')  # --> a)
        with open(env_path, 'a+') as fl:
            fl.write(input('b)\nEnter text to be appended to the file:\n'))
            fl.seek(0)
            p = fl.read().split('\n')
            """..."""
            print(*[str(i + 1) + ' : ' + p[i]
                    for i in range(len(p))], sep='\n')  # --> b)
            print(f'c)\nLast line of the file is:\n{p[-1]}')  # --> c)
            # --> d)
            print(f'd)\nFirst line from 10th character onwards:\n{p[0][10:]}')
        with open(env_path, 'r') as fl:
            p = fl.readlines()
            inp = int(input('e)\nEnter line no. to be read:\n'))
            if inp > len(p) or inp < -len(p) or inp == 0:
                print('The line no. you entered does not exist.')
            elif inp > 0:
                print(p[inp - 1].strip())  # --> e)
            else:
                print(p[inp].strip())
            fl.seek(0)
            p = (' '.join(fl.read().split('\n'))).split(' ')
            freq = {}
            for i in p:
                if i[0].lower() in freq:
                    freq[i[0].lower()] += 1
                else:
                    freq[i[0].lower()] = 1
            print('f)\n')
            print(*['Words beginning with ' + _ + ' : ' + str(freq[_])
                    for _ in freq], sep='\n')  # --> f)
# if we need to sort alphabetically, create var='abcd...xyz' and iterate
# over that printing <iter> : freq[<iter>]
    except FileNotFoundError:
        print('Checking local path')
        call('file1.txt')


def call(env_path=path):
    fl_create_ql(env_path)


call()
