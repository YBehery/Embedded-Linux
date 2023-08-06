#!/usr/bin/python3

#Shebang

user_dic={
    'Ahmed':1394,
    'Ali':6078,
    'Amr':9345
}
user_name=input('enter name:')
if user_name in user_dic:
    for i in range(3):
        password=int(input('enter password:'))
        if password==user_dic[user_name]:
            print(r'Welcome {}'.format(user_name))
            break
        else:
            print(r'incorrect entry {}'.format(i+1))
            if i==2:
                print('System Locked')
else:
    print('User not found')   