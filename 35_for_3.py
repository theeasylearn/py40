#for loop on dictionary
#make sum of runs scored by player 
cricket_scores = {
    "Rohit Sharma": 78,
    "Shubman Gill": 34,
    "Virat Kohli": 96,
    "Shreyas Iyer": 45,
    "KL Rahul": 62,
    "Hardik Pandya": 29,
    "Ravindra Jadeja": 51,
    "Kuldeep Yadav": 12,
    "Jasprit Bumrah": 7,
    "Mohammed Shami": 18,
    "Mohammed Siraj": 4
}
sum = 0
for player in cricket_scores:
    #player is key it is not value
    print(player,"has scored ",cricket_scores[player])
    sum = sum  + cricket_scores[player]

print("sum = ",sum)