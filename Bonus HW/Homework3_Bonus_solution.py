from elections_2002 import *
from matplotlib.pyplot import *

lowerBound = int(input("Please enter a lower bound for the threshold (barrage): "))
upperBound = int(input("Please enter an upper bound for the threshold (barrage): "))

chartResults = [0] * len(range(lowerBound,upperBound+1))
chartIndex = -1
for threshold in range(lowerBound, upperBound+1):
#for each threshold
    chartIndex += 1
    contryWideDeputyNumbers = [0]*len(partyNames)
    # initialize the deputy numbers for countrywide, initially all parties have 0 deputy
    for index in range(len(electoralDistricts)):
        districtName = electoralDistricts[index]
        deputy = districtDeputyNumbers[index]
        votes = voteNumbersOfParties[index]

        deputyNumbers = [0]*len(partyNames)
        # initialize the deputy numbers for local district, initially all parties have 0 deputy

        while(deputy > 0):
            tempVotes = [0]* len(votes)

            for i in range(len(tempVotes)):
                if countrywidePercentages[i] > threshold: # if country wide perc is above threshold
                    tempVotes[i] = votes[i] / (deputyNumbers[i]+1)
                    # otherwise leave it as 0

            maxValue = tempVotes[0]
            maxIndex = 0
            for i in range(len(tempVotes)):
                if tempVotes[i] > maxValue:
                    maxValue = tempVotes[i]
                    maxIndex = i

            # After finding the max voted party, increment its deputy number
            deputyNumbers[maxIndex] += 1
            contryWideDeputyNumbers[maxIndex] += 1
            deputy -= 1

    chartResults[chartIndex] = contryWideDeputyNumbers
    print("The result for threshold " + str(threshold) + " is " + str(contryWideDeputyNumbers))

for i in range(len(partyNames)):
    subResult = [0] * len(chartResults)
    for j in range(len(chartResults)):
        subResult[j] = chartResults[j][i]
    plot(range(lowerBound, upperBound+1), subResult, label = partyNames[i])
    
    
xlabel("barrage (threshold)")
ylabel("Seat Number")
legend()
show()       

