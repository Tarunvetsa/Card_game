def maxx(player):
    d ={}
    for i in player:
        if i[1] == '1':
            d[i] = h['10']
        else: 
            d[i] = h[i[1]]
    return max(d,key=d.get)
def minn(player):
    d ={}
    for i in player:
        if i[1] == '1':
            d[i] = h['10']
        else: 
            d[i] = h[i[1]]
            
    return min(d,key=d.get)
def mam(p):
    d = {}
    for i in p:
        if p[i][1]=='1':
            d[i] = h['10']
        else:
            d[i] = h[p[i][1]]
    return p[max(d,key=d.get)]
def aa(player,a):
    d = []
    for i in player:
        if  a == i[0]:
            d.append(i)
    return d 


# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product([2,3,4,5,6,7,8,9,10,'J','Q','K','A'],['S','H','D','C']))

# shuffle the cards
random.shuffle(deck)
for i in range(len(deck)):
    deck[i] =deck[i][1]+str(deck[i][0])

m = {'bot1':0,'bot2':0,'player':0,'bot3':0}
bot1,bot2,bot3,player = deck[:13],deck[13:26],deck[26:39],deck[39:52]
print(player)
'''where H-Hearts, C - Clubs, D - Diamonds and S - Spades
Similarly, A - Ace, K - King, Q - Queen, J - Joker'''
e = {'bot1':bot1,'bot2':bot2,'player':player,'bot3':bot3}

a_file = open('data.txt','wt')
a_file.write('Game1')
a_file.write('\n')
data = str(e)
a_file.write(data)

for i in e:
    for a in e[i]:
        if a[1] in 'QJKA':
            m[i] +=1

m['player'] = int(input('how many times u will win'))
print(m)
e = {'bot1':bot1,'bot2':bot2,'player':player,'bot3':bot3}
f = 0
a = int(input('give less than 4:(0-bot1,1-bot2,2-player,3-bot3)'))
print('call of players','bot1->',m['bot1'], 'bot2->',m['bot2'],'player->',m['player'], 'bot3->',m['bot3']) 
print('starts form',list(e.keys())[a])
h = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,"Q":11,'K':12,'A':13,'1':9}
x = {'bot1':0,'bot2':1,'player':2,'bot3':3}
q = {}
l = {'bot1':0,'bot2':0,'player':0,'bot3':0}
while f < 4:
    if a==4:
        a =0
    if a==2:
        c = input('Pick the card :')
        g = list(e.keys())[a]
    elif f==0: 
        g = list(e.keys())[a]
        c = maxx(e[g]) 
    else:
        g = list(e.keys())[a]
        if mam(q)[1] == '1':
            if h['10'] < h[maxx(aa(e[g],list(q.values())[0][0]))[1]]:
                    c = maxx(aa(e[g],list(q.values())[0][0]))
            else: 
                    c = minn(aa(e[g],list(q.values())[0][0]))
        elif h[mam(q)[1]] < h[maxx(aa(e[g],list(q.values())[0][0]))[1]]:
            c = maxx(aa(e[g],list(q.values())[0][0]))
        else:
            c = minn(aa(e[g],list(q.values())[0][0]))       
        c = maxx(aa(e[g],list(q.values())[0][0]))
    print(g,'->',c)
    e[g].remove(c)
    a+=1
    f+=1
    q[g] = c
d =[]
for i  in q:
    if q[i][1] =='1':
        d.append(h['10'])
        
    else:
        d.append(h[q[i][1]])
y =dict(zip(d,q))
z = y[max(y)]
l[z]+=1
print(z,'wins')

while len(player) >0:
    print(player)
    f = 0
    q = {}
    a = x[z]
    while f <4:
        if a==4:
            a =0
        if a==2:
            c = input('pick the card :')
            g = list(e.keys())[a]
        elif f==0: 
            g = list(e.keys())[a]
            c = maxx(e[g])
        else:
            g = list(e.keys())[a]
            if aa(e[g],list(q.values())[0][0]) == []:
                c = minn(e[g])
            elif mam(q)[1] == '1':
                if h['10'] < h[maxx(aa(e[g],list(q.values())[0][0]))[1]]:
                        c = maxx(aa(e[g],list(q.values())[0][0]))
                else: 
                        c = minn(aa(e[g],list(q.values())[0][0]))
            elif h[mam(q)[1]] < h[maxx(aa(e[g],list(q.values())[0][0]))[1]]:
                c = maxx(aa(e[g],list(q.values())[0][0]))
            else:
                c = minn(aa(e[g],list(q.values())[0][0])) 
        print(g,'->',c)
        e[g].remove(c)
        f+=1
        a+=1
        q[g] = c
        
    d =[]
    for i  in q:
        if q[i][1] =='1':
            d.append(h['10'])
        else:
            d.append(h[q[i][1]])
    y =dict(zip(d,q))
    z = y[max(y)]
    l[z] +=1
    print(z,'wins')
print(l)  
# scores of players
t = {}
w = {}
for i in l:
    if l[i] < m[i]:
        score = -10*m[i]
    else:
        score = 10*m[i] + (l[i]-m[i])
    t[score] = i
    w[i]= score
print(w)
a_file.write('\n')
a_file.write('scores:')
data = str(w)
a_file.write(data)
a_file.write('\n')
a_file.write(t[max(t)])
a_file.write('is winner')
a_file.write('\n')
print(t[max(t)],'is winner')

R = 2
while input('continue(Y/N):') == 'Y':
    
    deck = list(itertools.product([2,3,4,5,6,7,8,9,10,'J','Q','K','A'],['S','H','D','C']))
    random.shuffle(deck)
    for i in range(len(deck)):
        deck[i] =deck[i][1]+str(deck[i][0])

    m = {'bot1':0,'bot2':0,'player':0,'bot3':0}
    bot1,bot2,bot3,player = deck[:13],deck[13:26],deck[26:39],deck[39:52]
    print(player)
    '''where H-Hearts, C - Clubs, D - Diamonds and S - Spades
    Similarly, A - Ace, K - King, Q - Queen, J - Joker'''

    e = {'bot1':bot1,'bot2':bot2,'player':player,'bot3':bot3}
    a_file.write('\n')
    a_file.write('Game')
    a_file.write(str(R))
    a_file.write('\n')
    data = str(e)
    a_file.write(data)
    a_file.write('\n')
    for i in e:
        for a in e[i]:
            if a[1] in 'QJKA':
                m[i] +=1
    m['player'] = int(input('how many times u will win'))            
    print(m) 
    e = {'bot1':bot1,'bot2':bot2,'player':player,'bot3':bot3}
    f = 0
    a = int(input('give less than 4:(0-bot1,1-bot2,2-player,3-bot3)'))
    print('call of players','bot1->',m['bot1'], 'bot2->',m['bot2'],'player->',m['player'], 'bot3->',m['bot3']) 
    print('starts form',list(e.keys())[a])

    x = {'bot1':0,'bot2':1,'player':2,'bot3':3}
    q = {}
    l = {'bot1':0,'bot2':0,'player':0,'bot3':0}
    while f < 4:
        if a==4:
            a =0
        if a==2:
            c = input('pick the card :')
            g = list(e.keys())[a]
        elif f==0: 
            g = list(e.keys())[a]
            c = maxx(e[g]) 
        else:
            g = list(e.keys())[a]
            if mam(q)[1] == '1':
                if h['10'] < h[maxx(aa(e[g],list(q.values())[0][0]))[1]]:
                        c = maxx(aa(e[g],list(q.values())[0][0]))
                else: 
                        c = minn(aa(e[g],list(q.values())[0][0]))
            elif h[mam(q)[1]] < h[maxx(aa(e[g],list(q.values())[0][0]))[1]]:
                c = maxx(aa(e[g],list(q.values())[0][0]))
            else:
                c = minn(aa(e[g],list(q.values())[0][0]))       
        
        print(g,'->',c)
        e[g].remove(c)
        a+=1
        f+=1
        q[g] = c
    d =[]
    for i  in q:
        if q[i][1] =='1':
            d.append(h['10'])

        else:
            d.append(h[q[i][1]])
    y =dict(zip(d,q))
    z = y[max(y)]
    l[z]+=1
    print(z,'wins')

    while len(player) >0:
        print(player)
        f = 0
        q = {}
        a = x[z]
        while f <4:
            if a==4:
                a =0
            if a==2:
                c = input('pick the card :')
                g = list(e.keys())[a]
            elif f==0: 
                g = list(e.keys())[a]
                c = maxx(e[g]) 
            else:
                g = list(e.keys())[a]
                if aa(e[g],list(q.values())[0][0]) == []:
                    c = minn(e[g])
                elif mam(q)[1] == '1':
                    if h['10'] < h[maxx(aa(e[g],list(q.values())[0][0]))[1]]:
                            c = maxx(aa(e[g],list(q.values())[0][0]))
                    else: 
                            c = minn(aa(e[g],list(q.values())[0][0]))
                elif h[mam(q)[1]] < h[maxx(aa(e[g],list(q.values())[0][0]))[1]]:
                    c = maxx(aa(e[g],list(q.values())[0][0]))
                else:
                    c = minn(aa(e[g],list(q.values())[0][0])) 
            print(g,'->',c)
            e[g].remove(c)
            f+=1
            a+=1
            q[g] = c

        d =[]
        for i  in q:
            if q[i][1] =='1':
                d.append(h['10'])
            else:
                d.append(h[q[i][1]])
        y =dict(zip(d,q))
        z = y[max(y)]
        l[z] +=1
        print(z,'wins')
    print(l)  
    # scores of players
    o = {}
    p = {}
    for i in l:
        if l[i] < m[i]:
            score = -10*m[i]
        else:
            score = 10*m[i] + (l[i]-m[i])
        o[score] = i
        p[i] = score
    for i in w:
        w[i] += p[i]    
    print(p) 
    R=int(R)+1
    a_file.write('\n')
    a_file.write('scores:')
    data = str(p)
    a_file.write(data)
    a_file.write('\n')
    a_file.write(t[max(t)])
    a_file.write('is winner')
    a_file.write('\n')
    print(o[max(o)],'is winner')
print(w) 
data = str(w)
a_file.write(data)

w = max(w, key=w.get)
print(w,'win the series')
a_file.write('\n')
a_file.write(w)
a_file.write('win the series')
a_file.close()