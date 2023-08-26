pin=[0]
print(pin)
c=""
for i in range(8):
    c=input(f'enter pin {i} state:')
    if c.upper()=='IN':
        pin.append('0')
        
    elif c.upper()=='OUT':
        pin.append('1')
    else :
        c='ERROR'
        print(c)
        break
if c!='ERROR':
    D="".join(map(str,pin))
    file =open('~/Embedded-Linux/Python/Codes/Assignments/Python/lecture-3/ec.c','w')
    file.write('void INIT_PORTA_DIR(void)\n{\n\tDDRA=0b'+ D+';\n}') 
    file.close()     
