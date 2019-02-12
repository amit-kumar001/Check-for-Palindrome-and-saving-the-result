# def check(p):
#     return p[::-1]
# def same(p):
#     rev=reversed(p)
#     if p==rev:
#         return p
#     return rev
# p="wewew"
# ans=p
# if ans==rev:
#     print("codition 1")
# else:
#     print("condition2")

# value = ['wewew']
# #value = value.casefold()
# rev_list = reversed(value)
# if list(value) == list(rev_list):
#
#     print("It is palindrome",value)
# else:
#     print("It is not palindrome",rev_list)


value = ['wewew','aa']
#value = value.casefold()
rev_list = reversed(value)
if list(value) == list(rev_list):
    a =("It is palindrome", value)
    file=open("sample.txt","w")`
    for i in a:
        print(i)
        file.write("result is %s\n" %i)
    file.close()
# else:
#     print("It is not palindrome",rev_list)


