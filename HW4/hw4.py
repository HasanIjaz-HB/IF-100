def addFriendship(d, u1, u2):
    if u1 not in d:
        d[u1] = [u2]
    else:
        x = d[u1]
        x.append(u2)
        d[u1] = x

inFile = open("friendship.txt", "r")

d = {}
for line in inFile:
    infos = line.split("\t")
    user1 = int(infos[0])
    user2 = int(infos[1].replace("\n", ""))

    addFriendship(d, user1, user2)
    addFriendship(d, user2, user1)

user = int(input("Enter a user id to suggest some friends: "))
if user not in d:
    print("There is no such user")
else:
    friendDict = {}
    friends = d[user]
    for friend in friends:
        friendsOfFriend = d[friend]
        for f in friendsOfFriend:
            if f != user and f not in friends:
                if f not in friendDict:
                    friendDict[f] = 1
                else:
                    friendDict[f] = friendDict[f] + 1
    #print(friendDict)
    if len(friendDict) > 0:
        maxVal = max(friendDict.values())
        result = []
        for k,v in friendDict.items():
            if v == maxVal:
                result.append(k)
        #print(result)
        printingResult = ""
        while(len(result) > 0):
            minElement = min(result)
            printingResult = printingResult + str(minElement) + ", "
            result.remove(minElement)
        print(printingResult[:-2])
    else:
        print("There is no friend to suggest")
inFile.close()
