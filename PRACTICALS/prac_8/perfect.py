def generate_factors(n):
    ls=[]
    for i in range(1,n//2+1):
        if n%i==0:
            ls.append(i)
    ls.append(n)
    return ls

def is_prime_no(n):
    l= generate_factors(n)
    if len(l)==2:
        return True
    else:
        return False

def is_perfect_no(n):
    l=generate_factors(n)[:-1]
    sums=0
    for i in l:
        sums+=i
    if sums==n:
        return True
    else:
        return False
if __name__ == '__main__':
    inp=int(input('Enter no: '))
    print(f'Perfect No : {is_perfect_no(inp)}')
    print(f'Prime No : {is_prime_no(inp)}')
    print(f'Factors of {inp} are: {generate_factors(inp)}')
