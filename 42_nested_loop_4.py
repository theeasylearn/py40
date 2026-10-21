'''
        *
       * *
      * * *
     * * * *
    * * * * *
'''
for row in range (5,0,-1): # 5 times  outer loop
    #inner loop
    space = 1
    while space<row:
        print(" ",end=' ')
        space = space + 1
    for astrik in range(0,6-row):
        print("* ",end=' ')
    print("")

