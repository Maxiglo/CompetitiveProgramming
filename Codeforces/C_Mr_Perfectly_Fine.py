for _ in range(int(input())):
    io = []
    oi = []
    ii = []
    for i in range(int(input())):
        m, skills = input().split()
        # soit minimum 01 + 10 soit 11 
        if skills == '01':
            oi.append(int(m))
        elif skills == '10':
            io.append(int(m))
        elif skills == '11':
            ii.append(int(m))

    if len(io)>0 and len(oi)>0 and len(ii)>0:
        print(min(min(io)+min(oi), min(ii)))
    elif len(io)>0 and len(oi)>0:
        print(min(io)+min(oi))
    elif len(ii)>0:
        print(min(ii))
    else:
        print(-1)