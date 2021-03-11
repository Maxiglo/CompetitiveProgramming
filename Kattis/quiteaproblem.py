while True:
    try:
        ligne = input().lower()

        if 'problem' in ligne:
            print('yes')
        else:
            print('no')
    except EOFError:
        break