b = [' ']*9

def win(p):
    return (b[0]==b[1]==b[2]==p or b[3]==b[4]==b[5]==p or b[6]==b[7]==b[8]==p or
            b[0]==b[3]==b[6]==p or b[1]==b[4]==b[7]==p or b[2]==b[5]==b[8]==p or
            b[0]==b[4]==b[8]==p or b[2]==b[4]==b[6]==p)

p = 'X'
for _ in range(9):
    print(b[0:3], b[3:6], b[6:9])
    i = int(input(f"{p} move (0-8): "))
    b[i] = p
    if win(p):
        print("Player", p, "wins")
        break
    p = 'O' if p == 'X' else 'X'
else:
    print("Draw")
