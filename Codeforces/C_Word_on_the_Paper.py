for _ in range(int(input())):
    word = ''
    for i in range(8):
        s = input()
        for c in s:
            if c.isalpha():
                word += c 
    print(word)