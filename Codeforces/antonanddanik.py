n = int(input())

ligne = input()
ca= ligne.count('A')
cd= ligne.count('D')
if cd>ca:
    print('Danik')
elif ca>cd:
    print('Anton')
else:
    print('Friendship') 