import random

'''
probTransitionMatrix = [][]
probFlipMatrix = [][]
'''

ProbXAgian = .75
ProbXToY = .25
ProbYAgain = .1
ProbYtoX = .9

x = 0
y = 1

xHeads = .4
xTails = .6
yHeads = .8
yTails = .2

output1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
output2 = [1, 0, 1, 0, 1, 0, 0, 0, 1, 1]
output3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Assumption coin starts Y
i = 0

while i < len(output1)-1:
    if i == 0:
        if output1[0] == 1:
            if yHeads > xHeads:
                coin = y
                print coin
            else:
                coin = x
                print coin
        else:
            if yTails > xTails:
                coin = y
                print coin
            else:
                coin = x
                print coin
    
    i += 1
    
    print "i = ",i
    '''
    print len(output1)
    print output1
    '''
    if output1[i] == 1:
        #print "iterate"
        if coin == x:
            if ProbXAgian*xHeads > ProbXToY*yHeads:
                coin = x
                print coin
            else:
                coin = y
                print coin
        else:
            if ProbYAgain*yHeads > ProbYtoX*xHeads:
                coin = y
                print coin
            else:
                coin = x
                print coin
        
    else:
        if coin == x:
            if ProbXAgian*xTails > ProbXToY*yTails:
                coin = x
                print coin
            else:
                coin = y
                print coin
        else:
            if ProbYAgain*yTails > ProbYtoX*xTails:
                coin = y
                print coin
            else:
                coin = x
                print coin
''' 
while i <= len(output1):
    i += 1
    if coin == y:
        print coin 
        print ProbXToY*100
        var = random.randint(0, 100)
        print float(var)
        if float(var) <= ProbYtoX*100:
            coin = x
        else:
            coin = y
    
    if coin == x:
        print coin 
        print ProbXToY*100
        var = random.randint(0, 100)
        print float(var)
        if float(var) <= ProbXToY*100:
            coin = x
        else:
            coin = y
    
'''