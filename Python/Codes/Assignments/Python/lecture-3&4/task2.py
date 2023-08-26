shopping=['eggs','milk','bread','flour']

with open('Embedded-Linux/Python/Codes/Assignments/Python/lecture-3/file2.txt','w') as file:
    for i in shopping:
        file.writelines(str(1+shopping.index(i))+'-'+i+'\n')

print(open('Embedded-Linux/Python/Codes/Assignments/Python/lecture-3/file2.txt','r').read())