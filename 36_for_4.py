#example of for loop on string
# count no of words 
name = "the easylearn academy bhavnagar 364001"
word = 1
for letter in name:
    #print(letter,end=' ')
    if letter == ' ':
        word = word + 1

print("words = ",word)