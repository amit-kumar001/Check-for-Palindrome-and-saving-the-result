## Check for Palindrome and saving the result  
## Key feature
<ol>
<li> Define list with it's items, every item in the list is checked for the condtion (<strong>palindrome or not</strong>)</li>
<li> Use <strong>for loop</strong>, so that we can iterate the list</li>
<li> Use advanced slice operation [start:end:step] with start,end and step size. This slice operation reverses the string.</li>
<li> Use try and except block to handle exceptions.Try statement is executed as a “normal” part of the program. 
     The code that follows the except statement is the program's response to any exceptions in the preceding try clause </li>
    </ol>
 
 ## Coding
 ## To check palindrome items
 
 ```
value = ['wewe','aa','abcd','121','111']
empty_list = []
empty_list_2 =[]
for i in value:
    rev_string = i[::-1] 
                   
    try:
        if i == rev_string:
            print("Successful is operation")
            empty_list.append(rev_string)
        else:
            raise Exception("Raise error")

    except Exception as e:
        print(e)
        
```

## Store result in file

```
with open('palindrome.txt','w+') as f:
    for i in empty_list:
        f.write('%s\n' %i)
    f.close()

with open('palindrome_not.txt','w+') as f:
    for i in empty_list_2:
        f.write('%s\n' %i)
    f.close()
 ```  
 
 ## How to run this file
Since this is a python file, hence it can be run using following command

  ```
  python file_handling_with_list.py
  python3 file_handling_with_list.py
  ```
 
 
    
