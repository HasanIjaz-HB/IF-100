#Hasan Ijaz

from elections_2002 import*
from matplotlib.pyplot import*
LB=int(input("Please​ ​enter​ ​a​ ​lower​ ​bound​ ​for​ ​the​ ​threshold​ ​(barrage) : "))
UB=int(input("Please​ ​enter​ ​a​ ​lower​ ​bound​ ​for​ ​the​ ​threshold​ ​(barrage) : "))
def D(x,z,i):
    for index in range(len(partyNames)):
        if z < countrywidePercentages[index]:
            N[index]=voteNumbersOfParties[i][index]/(s[index]+1)
        else:
            N[index]=0
    mx=max(N)
    mxidx=N.index(mx)
    s[mxidx]+=1

def computeSeats(L, party_index):
    party_list = [0]*len(L)
    for p_index in range(len(L)):
        party_list[p_index] = L[p_index][party_index]
    return party_list

s=[0]*len(partyNames)
N=[0]*len(partyNames)
totals=[0]*len(partyNames)
l = [[0] * len(partyNames)] * (UB - LB + 1)
threshold=[0]*(UB-LB+1)

for z in range(LB,UB+1):
    totals=[0]*len(partyNames)
    for i in range(0,81):
        s=[0]*len(partyNames)
        for j in range(len(voteNumbersOfParties[i])):
            N[j]=voteNumbersOfParties[i][j]
        for x in range(0,districtDeputyNumbers[i]):
            D(N,z,i)
        for u in range(len(s)):
            totals[u]+=s[u]
    print("The​ ​result​ ​for​ ​threshold​",z,"is", totals)
    
    l[z - LB] = totals
#print(l)
for w in range(UB-LB +1):
    threshold[w]=LB
    LB+=1
    
#print(threshold)

r=[0]*len(partyNames)
for row in r:
    row = [0]*len(threshold)

for index in range(len(r)):
    r[index] = computeSeats(l, index)

for index in range(len(r)):
    plot(threshold, r[index], label=partyNames[index])

legend(loc='best')
show()



