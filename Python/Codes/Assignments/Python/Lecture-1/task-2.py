vowels=('A','E','I','O','U')
c=input('enter character :')
for i in vowels:
    if i==c.upper():
        print('Is Vowel')
        break
    elif i=='U':
        print('Not Vowel')
        
    