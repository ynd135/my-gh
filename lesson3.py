##s = """
##Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
##Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
##Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
##Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
##"""
##print(s)
##s1 = "Hello World!"
##print(s1 [0])
##print(s1[6:])
##print(s1[::2])
####s1[-1] = ' A'
####print(s1)
##s2 = "Hello World!"
##s2 = s2 [0:-1] + 'A'
##print(s2)
##
##grocery = 'Milk, Chicken, Bread, Butter'
### maxsplit: 2
##print(grocery.split(', ', 2))
### maxsplit: 1
##print(grocery.split(', ', 1))
### maxsplit: 5
##print(grocery.split(', ', 5))
### maxsplit: 0
##print(grocery.split(', ', 0))
##
##print("-".join("Python"))
##
##s3 = input("Enter symbols: ")
##print(s3.split())
##
##s4 = 'red blue yellow green pink'
##print(s4.find('green'))
##print(s4.find('violet'))
##
##num1 = 10
##num2 = 15
##print(('Our numbers: {0}, {1}').format(num1,num2))
##

user_s = input("Enter: ")
num_up = 0
num_low = 0

for i in user_s:
    if i.islower():
        num_low +=1
    elif i.isupper():
        num_up +=1

if num_low >= num_up:
    print(user_s.lower())
else:
    print(user_s.upper())

    
    






