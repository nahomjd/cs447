import json
#Read in first 2 lines to set bulbs and switches
f = open("out-no1.txt", "r")
#f.close()

switchesS = f.readline()
bulbsS = f.readline()

switches = int(switchesS)
bulbs = int(bulbsS)

AmountNodes = 2*switches

read = f.read()
lines = read.split("\n")
print len(lines)
i = 0 #line node

node = []
for row in lines:
    switch = row.split(" ")
    print switch[0], switch[1]
    #node[i] = switch[0]
    node.append([switch[0], switch[1]])
    #node[i] = switch[1]
    #print switch[1]

print node
    
print switches
print bulbs



#print read


#Read in every line and save them in nodes

