from lab3 import XC3Tree

print ("XC3 Tree:")
for i in range(26):
    t = XC3Tree(i)
    print(i,t.getHeight(),t.getNodeNum())   

def nodes(i):
    #i >= 0
    if i == 0:
        return 1
    if i == 1:
        return 2
    return nodes(i- 1) + nodes(i-2)

print ("Nodes:")
for i in range(26):
    n = nodes(i)
    print(i,n)   