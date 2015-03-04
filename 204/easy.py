phrase = 'Eye of newt'

with open('macbeth.txt', 'r') as f:
    lines = f.read().split('\n\n')
    for line in lines:
        if phrase in line:
            for x in line.split('\n'):
                if x.startswith('    '):
                    print x[4:]
            break
