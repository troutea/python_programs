# jabber = open('Jabberwocky.txt', 'r')

# for line in jabber:
#     #print(line, end='')
#     print(line.strip())
#    # print(len(line))
    
# jabber.close()

with open('Jabberwocky.txt', 'r') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break
    
            
