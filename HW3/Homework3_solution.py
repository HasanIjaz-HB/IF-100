from elections_2002 import *

index = int(input("Please enter an index between 0 and 80 (both are inclusive): "))

if 0 <= index <= 80:
    districtName = electoralDistricts[index]
    deputy = districtDeputyNumbers[index]
    votes = voteNumbersOfParties[index]

    deputyNumbers = [0]*len(partyNames)
    # initialize the deputy numbers, initially all parties have 0 deputy

    while(deputy > 0):
        tempVotes = [0]* len(votes)

        for i in range(len(tempVotes)):
            tempVotes[i] = votes[i] / (deputyNumbers[i]+1)

        maxValue = tempVotes[0]
        maxIndex = 0
        for i in range(len(tempVotes)):
            if tempVotes[i] > maxValue:
                maxValue = tempVotes[i]
                maxIndex = i

        # After finding the max voted party, increment its deputy number
        deputyNumbers[maxIndex] += 1
        deputy -= 1

    print("Results for " + districtName + " as follows:")
    for i in range(len(tempVotes)):
        print(partyNames[i] + ": " + str(deputyNumbers[i]))
    

else:
    print("You entered an invalid input!!!")
