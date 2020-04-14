import random
from faker import Faker

def random_name_list(num):
    return [Faker().first_name() for i in range(num)]

def random_name_tuple(num):
    # this is an example of a list comprehension
    return [Faker().first_name() for i in range(num)]

def random_name():
    return Faker().first_name()

def sum_of(s1,s2,s3):
    return s1+s2+s3

def is_magic(s):
    top = sum_of(s[0],s[1],s[2]) # top row
    middle = sum_of(s[3],s[4],s[5]) # bottom row
    bottom = sum_of(s[6],s[7],s[8]) # bottom row
    first_col = sum_of(s[0],s[3],s[6]) # first column
    second_col = sum_of(s[1],s[4],s[7]) # second column
    third_col = sum_of(s[2],s[5],s[8]) # third column
    diag1 = sum_of(s[0],s[4],s[8]) # third column
    diag2 = sum_of(s[2],s[4],s[6]) # third column
    v = [top,middle,bottom,first_col,second_col,third_col,diag1,diag2]
    is_lo_shu = True
    last = v[0]
    for value in v[1:]:
        if value != last:
            is_lo_shu = False
            break
        last = value
    return is_lo_shu

def get_matrix():
    nums = [i for i in range(1,10)]
    random.shuffle(nums)
    return nums

def as_matrix(m):
    return [m[0:3],m[3:6],m[6:]]

def lo_shu():
    m = get_matrix()
    count = 0
    while not is_magic(m):
        m = get_matrix()
        count += 1
    print(f'took {count} {m} {[(i) for i in as_matrix(m)]}')


def spiralPrint(a):
    m = len(a)    # rows
    n = len(a[0]) # columns
    print(f'rows={m},cols={n} a={a}')
    k = 0 # row index
    l = 0 # column index
    while k < m and l < n:
        # print the top row
        for i in range(l,n):
            print(f'{a[k][i]} ',sep=' ',end='')
        k += 1
        # print the last column next element down
        for i in range(k,m):
            print(f'{a[i][n-1]} ',sep=' ',end='')
        n -= 1
        if k < m:  # we are not done
            # print the last row next element to the left
            for i in range(n-1,l-1,-1):
                print(f'{a[m-1][i]} ',sep=' ',end='')
            m-=1
        if l < n:
            # print the first column next element up 
            for i in range(m-1,k-1,-1):
                print(f'{a[i][l]} ',sep=' ',end='')
            l += 1
    print()

def rotate_list(a,i):
    c = a
    for i in range(i):
        f = c[0:4] + c[5:]    # extract the outside
        f = [f[-1]] + f[:-1]  # rotate the outside
        c = f[0:4] +[5] + f[4:] # rebuild the list
    return c