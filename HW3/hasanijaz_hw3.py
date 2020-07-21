#Hasan Ijaz
from elections_2002 import*
Id=int(input("Please​ ​enter​ ​an​ ​index​ ​between​ ​0​ ​and​ ​80​ ​(both​ ​are​ ​inclusive): "))

def D(x,y):
    mx=max(N)
    mxidx=N.index(mx)
    s[mxidx]+=1
    N[mxidx]=voteNumbersOfParties[Id][mxidx]/(s[mxidx]+1)
s=[0]*len(partyNames)
N=[0]*len(partyNames)

if (Id <0 or Id >80):
    print("You​ ​entered​ ​an​ ​invalid​ ​input!!!")
else:
    for i in range(len(voteNumbersOfParties[Id])):
        N[i]=voteNumbersOfParties[Id][i]
    for i in range(0,districtDeputyNumbers[Id]):
        D(N,Id)
    print("Results for",electoralDistricts[Id],"as follows:" )
    for i in range(0,len(partyNames)):
        print(partyNames[i]+":",s[i])

            
            
            

