'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
for row in range (5,0,-1): # 5 times  outer loop
    #inner loop
    for space in range(1,row): 
        print(" ",end=' ')
    for astrik in range(0,6-row):
        print("*",end=' ')
    print("")

