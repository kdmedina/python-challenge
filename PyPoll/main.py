import os
import csv

#Identifies poll data
file = os.path.join('Resources', 'election_data.csv')

#Creates dictionary for candidate name and vote count.
poll = {}

#Sets variable, total votes, to zero for count.
total_votes = 0

#Gets data file
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    #Skips header line
    next(csvread, None)

    #Creates dictionary from file using column 3 as keys, using each name only once.
    #Keeps a total vote count by counting up 1 for each loop
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
    #Create empty list for candidates and his/her vote count
candidates = []
num_votes = []

#Takes dictionary keys and values and put into the lists
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

#Creates vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 3))


clean_data = list(zip(candidates, num_votes, vote_percent))

#Creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

#Makes winner_list 
winner = winner_list[0]

#Only runs if there is a tie and puts additional winners into string 
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#Prints to file
output_file = os.path.join('election_results.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#Prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())