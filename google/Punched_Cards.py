for case in range(int(input())):
    r, c = map(int, input().split())
    print(f'Case #{case+1}:')
    # je suis con il faut réfléchir et pas faire une méthode de bourrin
    for line in range(r):
        if line == 0:
            print('..' + '+-'*(c-1)+'+')
            print('..' + '|.'*(c-1)+'|')       
        else:
            print('+-'*(c)+'+')
            print('|.'*(c)+'|')
    print('+-' * c + '+') 
