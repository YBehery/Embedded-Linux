#!usr/bin/python3

user_input=input('enter list of numbers\n')
#split string into list of strings seperated by space
ls=user_input.split()
#convert string list to ints
for i in range(len(ls)):
    ls[i]=int(ls[i])
num=int(input('enter number to get number of occurences :'))
print(ls.count(num))