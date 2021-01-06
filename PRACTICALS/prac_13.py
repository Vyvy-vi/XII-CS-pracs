import time
s=[]
top= None
def ui():
    inp = int(input('\nPress 1 to play and add ring.\n\
Press 2 to Skip chance.\n\
Press 3 to Quit Game.\n'))
    if inp == 1:
        ring = eval(input('Enter size of ring: '))
        print(add_ring(ring))
        print(show_stack())
    elif inp == 2:
        print('You have missed this chance.')
        print(show_stack())
    elif inp == 3:
        print('bye')
        return
    time.sleep(2)
    ui() 
def add_ring(ring):
    print('Adding ring...')
    if isempty(s):
        push(s, ring)
        return 'RING HAS BEEN ADDED.'
    substack =[]
    peeked_ring = peek()
    while ring < peeked_ring or peeked_ring == 'UNDERFLOW':
        push(substack, stk_pop(s))
        peeked_ring = peek()
        if peeked_ring == 'UNDERFLOW':
            break
    push(s, ring)
    while not isempty(substack):
        push(s, stk_pop(substack))
    return 'RING HAS BEEN ADDED.'
def isempty(stk):
    if len(stk) == 0:
        return True
    else:
        return False
def push(stk,el):
    stk.append(el)

def stk_pop(stk):
    if len(stk) == 0:
        return 'UNDERFLOW'
    else:
        p = stk.pop()
        return p
def peek():
    if len(s) == 0:
        return 'UNDERFLOW'
    else:
        top = len(s)-1
        return s[top]
def show_stack():
    return f'The current stack is {s}\n'
ui()
