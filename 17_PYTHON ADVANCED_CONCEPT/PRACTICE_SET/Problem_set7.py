# 7. Walrus Operator
#     1. Use the walrus operator to read input until the user enters "quit" . Print each
#     input as it is entered.
#     2. Use the walrus operator in a list comprehension to store lengths of words
#     from ["python", "rocks", "ai"] in a list while filtering out words shorter
#     than 4 characters.
 
# while True:
#     if word:= input("Enter your word : ") =="quit":
#         break

mylist = ["python", "rocks", "ai"]
total =0
while total==False:
    for i in range(0,len(mylist)): 
        if total := len(mylist[i])==2:
            print(len(mylist[i]))
            break
        
        else:
            print("the word is = ", {mylist[i]})
            print(len(mylist[i]))
