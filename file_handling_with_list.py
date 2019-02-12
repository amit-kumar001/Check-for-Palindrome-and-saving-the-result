value = ['wewe','aa','abcd','121','111']
empty_list = [] #empty list
empty_list_2 =[]#empty list
for i in value:
    rev_string = i[::-1] #operation for reverses the string.
    try:
        if i == rev_string:
            print("Successful is operation")
            empty_list.append(rev_string) # append() method takes every single item and adds it in the empty list
        else:
            raise Exception("Raise error")#raise an exception so that it can later be caught via an except block

    except Exception as e: 
        print(e)
        empty_list_2.append(i)
print("Please see the value in list which are palindrome:",empty_list)
print("Please see the value in list which are not palindrome:",empty_list_2)


#####Storing the result in the file#########

with open('palindrome.txt','w+') as f:# create file to store result
    for i in empty_list:
        f.write('%s\n' %i)# %s- for string, %i - store value of i
    f.close()

with open('palindrome_not.txt','w+') as f:
    for i in empty_list_2:
        f.write('%s\n' %i)
    f.close()


