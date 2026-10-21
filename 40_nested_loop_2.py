'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
for row in range (5,0,-1): # 5 times  outer loop
    #inner loop
    for astrik in range(0,row): 
        print(f"{astrik+1}",end=' ')
    print("")

